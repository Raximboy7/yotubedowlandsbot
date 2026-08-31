"""YouTube Downloader Bot.

Send the bot a YouTube link and choose video or audio; it downloads the media
with yt-dlp and uploads the file back into the chat.

Run:
    cp .env.example .env      # add BOT_TOKEN
    pip install -r requirements.txt
    python main.py
"""
from __future__ import annotations

import logging
import os
import re
import tempfile
from pathlib import Path

import telebot
import yt_dlp
from dotenv import load_dotenv
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Copy .env.example to .env and fill it in.")

# Telegram refuses uploads larger than 50 MB from a normal bot.
MAX_UPLOAD_BYTES = 50 * 1024 * 1024

YOUTUBE_RE = re.compile(
    r"https?://(?:www\.|m\.)?(?:youtube\.com/(?:watch\?v=|shorts/|live/)|youtu\.be/)[\w\-]+",
    re.IGNORECASE,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
)
log = logging.getLogger("ytbot")

bot = telebot.TeleBot(BOT_TOKEN)

# url cache keyed by callback id, so the callback payload stays short
_pending: dict[str, str] = {}


def _human(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def _download(url: str, audio_only: bool, target_dir: Path) -> Path:
    """Download `url` into `target_dir` and return the resulting file path."""
    options = {
        "outtmpl": str(target_dir / "%(title).80s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "restrictfilenames": True,
    }
    if audio_only:
        options.update(
            {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
        )
    else:
        # cap the height so the file usually fits Telegram's upload limit
        options["format"] = "best[ext=mp4][height<=720]/best[ext=mp4]/best"

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        path = Path(ydl.prepare_filename(info))

    if audio_only:
        path = path.with_suffix(".mp3")
    return path


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: Message) -> None:
    bot.reply_to(
        message,
        "👋 Salom!\n\n"
        "YouTube havolasini yuboring — men uni video yoki audio (MP3) "
        "ko'rinishida yuklab beraman.\n\n"
        "⚠️ Telegram cheklovi tufayli fayl hajmi 50 MB dan oshmasligi kerak.",
    )


@bot.message_handler(func=lambda m: True, content_types=["text"])
def handle_link(message: Message) -> None:
    match = YOUTUBE_RE.search(message.text or "")
    if not match:
        bot.reply_to(message, "❌ Bu YouTube havolasiga o'xshamadi. Qaytadan yuboring.")
        return

    key = str(message.message_id)
    _pending[key] = match.group(0)

    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("🎬 Video", callback_data=f"video:{key}"),
        InlineKeyboardButton("🎵 Audio (MP3)", callback_data=f"audio:{key}"),
    )
    bot.reply_to(message, "Qaysi formatda yuklab beray?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: ":" in call.data)
def handle_choice(call) -> None:
    kind, key = call.data.split(":", 1)
    url = _pending.pop(key, None)
    if not url:
        bot.answer_callback_query(call.id, "Havola eskirdi, qaytadan yuboring.")
        return

    bot.answer_callback_query(call.id)
    status = bot.edit_message_text(
        "⏳ Yuklanmoqda…",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
    )

    with tempfile.TemporaryDirectory() as tmp:
        try:
            path = _download(url, audio_only=(kind == "audio"), target_dir=Path(tmp))
        except Exception as exc:  # noqa: BLE001 — surface any yt-dlp failure to the user
            log.exception("download failed: %s", url)
            bot.edit_message_text(
                f"❌ Yuklab bo'lmadi: {exc}",
                chat_id=status.chat.id,
                message_id=status.message_id,
            )
            return

        size = path.stat().st_size
        if size > MAX_UPLOAD_BYTES:
            bot.edit_message_text(
                f"❌ Fayl juda katta ({_human(size)}). "
                f"Telegram orqali {_human(MAX_UPLOAD_BYTES)} gacha yuborish mumkin.",
                chat_id=status.chat.id,
                message_id=status.message_id,
            )
            return

        bot.edit_message_text(
            "📤 Yuborilmoqda…", chat_id=status.chat.id, message_id=status.message_id
        )
        with path.open("rb") as media:
            if kind == "audio":
                bot.send_audio(call.message.chat.id, media, title=path.stem)
            else:
                bot.send_video(call.message.chat.id, media, caption=path.stem)

    bot.delete_message(status.chat.id, status.message_id)


if __name__ == "__main__":
    log.info("bot started")
    bot.infinity_polling(skip_pending=True)
