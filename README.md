<div align="center">

# 📥 YouTube Downloader Bot

**A Telegram bot that downloads YouTube video and audio straight into the chat**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="python" />
  <img src="https://img.shields.io/badge/Telegram_Bot-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="telegram" />
  <img src="https://img.shields.io/badge/yt--dlp-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="ytdlp" />
</p>

<p>
  <a href="https://github.com/Raximboy7/yotubedowlandsbot/stargazers"><img src="https://img.shields.io/github/stars/Raximboy7/yotubedowlandsbot?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="stars" /></a>
  <a href="https://github.com/Raximboy7/yotubedowlandsbot/commits"><img src="https://img.shields.io/github/last-commit/Raximboy7/yotubedowlandsbot?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="last commit" /></a>
  <a href="https://github.com/Raximboy7/yotubedowlandsbot/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-8B5CF6?style=flat-square&labelColor=0D1117" alt="license" /></a>
</p>

</div>

<p align="center">
  <img src="bot.png" width="320" alt="Bot preview" />
</p>

---


## 📖 Overview

Send the bot a YouTube link and pick a format — it fetches the media with `yt-dlp`, converts it if needed and uploads the file back to Telegram. Built with `pyTelegramBotAPI`, it runs on a single process and needs nothing but a bot token.


## ✨ Features

- 🎬 **Video download** — MP4 in the best available quality
- 🎵 **Audio extraction** — MP3 for music and podcasts
- 🔗 **Link detection** — paste a URL, the bot does the rest
- ⚡ **Inline keyboards** for choosing the format
- 🧹 **Automatic cleanup** of temporary files after upload
- 🔐 **Token from environment** — no secret ever touches the repository



## 🚀 Getting Started

```bash
# 1 — clone
git clone https://github.com/Raximboy7/yotubedowlandsbot.git
cd yotubedowlandsbot

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # add your token

# run
python main.py
```


## 🔧 Configuration

Copy `.env.example` to `.env` and fill in your own values. **`.env` is git-ignored — never commit it.**

| Variable | Description | Default |
|---|---|---|
| `BOT_TOKEN` | Telegram bot token from @BotFather | — |


## 📁 Project Structure

```
yotubedowlandsbot/
├── main.py            # bot entry point, handlers
├── requirements.txt
├── .env.example
├── bot.png            # preview image
└── .gitignore
```


## 🗓 Roadmap

- [ ] Playlist support
- [ ] Progress bar while downloading
- [ ] Split files larger than Telegram's 50 MB upload limit
- [ ] Instagram / TikTok links
- [ ] Docker image + systemd unit


---

<details>
<summary><b>🇺🇿 &nbsp;O'zbekcha tavsif</b></summary>

<br/>

## 📖 Loyiha haqida

Botga YouTube havolasini yuborasiz, formatni tanlaysiz — bot `yt-dlp` orqali yuklab olib, faylni Telegramga qaytaradi. `pyTelegramBotAPI` asosida yozilgan, ishlashi uchun faqat bot tokeni kerak.

## 🚀 Ishga tushirish

```bash
# 1 — clone
git clone https://github.com/Raximboy7/yotubedowlandsbot.git
cd yotubedowlandsbot

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # add your token

# run
python main.py
```

</details>

---

## 🤝 Contributing

Issue va Pull Request'lar ochiq. Katta o'zgarishdan oldin issue orqali muhokama qiling.

## 📄 License

MIT — batafsil [`LICENSE`](LICENSE) faylida.

## 👤 Author

<table>
<tr>
<td align="center">
<a href="https://github.com/Raximboy7"><img src="https://github.com/Raximboy7.png" width="80" alt="Raximboy Ibrohimov" /></a>
</td>
<td>

**Raximboy Ibrohimov**<br/>
Backend &amp; Mobile Developer · Tashkent, Uzbekistan 🇺🇿

[![Portfolio](https://img.shields.io/badge/Portfolio-8B5CF6?style=flat-square&logo=googlechrome&logoColor=white)](https://ibrohimov-dev.uz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raximboy-ibroximov-a75855268/)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Raximboy7)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:raximboy4200@gmail.com)

</td>
</tr>
</table>

<div align="center">
<sub>⭐ Foydali bo'lsa, yulduzcha qoldiring!</sub>
</div>
