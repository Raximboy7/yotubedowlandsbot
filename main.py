from pytube import YouTube
import telebot

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! YouTube video URL'ini yuboring va men uni sizga yuklab beraman.")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    url = message.text
    if "youtube.com/" in url or "youtu.be/" in url:
        bot.reply_to(message, "Video yuklab olinmoqda...")
        try:
            yt = YouTube(url)
            video = yt.streams.filter(file_extension='mp4').first()
            video.download('videos/')
            bot.reply_to(message, "Video muvaffaqiyatli yuklab olindi!")
        except Exception as e:
            bot.reply_to(message, f"Xatolik yuz berdi: {e}")
    else:
        bot.reply_to(message, "Iltimos, yaroqli bir YouTube URL'ini yuboring.")

bot.polling()
