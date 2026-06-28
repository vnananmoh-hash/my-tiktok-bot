import os
from flask import Flask
from threading import Thread
import telebot

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- هنا تحط التوكن تاعك ---
BOT_TOKEN = "8738979905:AAHDzJhDXtIQvAf0ttekyyFmkgWogWs5U4g" 
# ---------------------------

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am ready.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "tiktok.com" in message.text:
        bot.reply_to(message, "Processing your request...")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
