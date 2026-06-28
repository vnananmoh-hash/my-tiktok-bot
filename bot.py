import telebot
import yt_dlp
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Bot is running!"
def run(): app.run(host='0.0.0.0', port=8080)
Thread(target=run).start()

BOT_TOKEN = "8738979905:AAHDzJhDXtIQvAf0ttekyyFmkgWogWs5U4g"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send me a link to download.")

@bot.message_handler(func=lambda message: message.text.startswith("http"))
def download_video(message):
    url = message.text
    msg = bot.reply_to(message, "Processing...")
    try:
        ydl_opts = {'outtmpl': 'video.mp4', 'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        with open('video.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)
        bot.delete_message(message.chat.id, msg.message_id)
        os.remove('video.mp4')
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.infinity_polling()
