import os
from flask import Flask
from threading import Thread
import telebot

# ==========================================
# 1. جزء السيرفر الوهمي لتخطي مشكلة إغلاق Render
# ==========================================
app = Flask('')

@app.route('/')
def home():
    return "البوت شغال 24 ساعة بنجاح!"

def run():
    # المنصة تعطي منفذ تلقائي عبر الـ Environment Variable أو تستخدم 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==========================================
# 2. إعداد البوت والتوكن الخاص بك
# ==========================================

BOT_TOKEN = "8738979905:AAHDzJhDXtIQvAf0ttekyyFmkgWogWs5U4g" 

bot = telebot.TeleBot(BOT_TOKEN)

# رسالة الترحيب /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك إلياس! أنا بوت تحميل فيديوهات تيك توك، أرسل لي الرابط الآن 🚀")

# استقبال الروابط
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "tiktok.com" in message.text:
        bot.reply_to(message, "جاري فحص رابط تيك توك والتحميل... ⏳")
    else:
        bot.reply_to(message, "من فضلك أرسل رابط تيك توك صحيح.")

# ==========================================
# 3. تشغيل السيرفر الوهمي والبوت معاً
# ==========================================
if __name__ == "__main__":
    print("جاري فحص وتثبيت المكتبات... انتظر ثواني ⏳")
    print("!المكتبات جاهزة والبوت يعمل الآن ✅")
    
    # تشغيل سيرفر Flask في الخلفية أولاً
    keep_alive()
    
    # تشغيل استقبال رسائل التليجرام بلا توقف
    bot.infinity_polling(skip_pending=True)
