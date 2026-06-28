import os
from flask import Flask
from threading import Thread
import telebot

app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

BOT_TOKEN = "8738979905:AAHDzJhDXtIQvAf0ttekyyFmkgWogWs5U4g" 

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am ready to download TikTok videos.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "tiktok.com" in message.text:
        bot.reply_to(message, "Processing your request...")
    else:
        bot.reply_to(message, "Please send a valid TikTok link.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling(skip_pending=True)
