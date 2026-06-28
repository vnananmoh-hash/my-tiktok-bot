import os
import subprocess
import sys

# دالة لتثبيت المكتبات تلقائياً إذا كانت ناقصة
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("⏳ جاري فحص وتثبيت المكتبات الناقصة... انتظر ثواني")
try:
    import telebot
except ImportError:
    install('pyTelegramBotAPI')
    import telebot

try:
    import yt_dlp
except ImportError:
    install('yt-dlp')
    import yt_dlp

# --- بداية كود البوت بعد التأكد من المكتبات ---

TOKEN = "8738979905:AAHDzJhDXtIQvAf0ttekyyFmkgWogWs5U4g"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def download_msg(m):
    if "http" in m.text:
        wait = bot.reply_to(m, "⏳ جاري التحميل...")
        opts = {'format': 'best', 'outtmpl': 'v.mp4', 'quiet': True}
        try:
            if os.path.exists("v.mp4"): os.remove("v.mp4")
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([m.text])
            with open("v.mp4", 'rb') as v:
                bot.send_video(m.chat.id, v, caption="✅ تم التحميل!")
            bot.delete_message(m.chat.id, wait.message_id)
            os.remove("v.mp4")
        except Exception as e:
            bot.edit_message_text(f"❌ خطأ: {str(e)}", m.chat.id, wait.message_id)
    else:
        bot.reply_to(m, "أرسل رابط فيديو لتحميله.")

print("✅ المكتبات جاهزة والبوت يعمل الآن!")
bot.polling(none_stop=True)
