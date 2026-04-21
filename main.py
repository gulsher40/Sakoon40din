import os
import logging
import asyncio
from datetime import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import pytz

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get("TOKEN")
CHAT_IDS = set() # Yahan sab users ki ID save hogi

# 40 Din ka Sabaq List
SABAQ = [
    "Day 1: Aaj sirf 'Alhamdulillah' 100 baar dil se kaho. Har haal mein shukr.",
    "Day 2: Aaj kisi 1 shakhs ko maaf kar do. Dil ka bojh halka ho jayega.",
    "Day 3: Aaj 5 min khamoshi se baitho. Sirf saans ko mehsoos karo.",
    "Day 4: Aaj 3 baar Durood Shareef padho. Rooh ko sukoon milega.",
    "Day 5: Aaj kisi bhooke ko khana khilao ya uski dua lo.",
    "Day 6: Aaj apni maa/baap ke liye dil se dua karo.",
    "Day 7: Aaj 'La hawla wala quwwata illa billah' 33 baar padho.",
    "Day 8: Aaj phone se 1 ghanta door raho. Khud se milo.",
    "Day 9: Aaj 'Ya Salaamu' 100 baar padho. Dil ko salaamti milegi.",
    "Day 10: Aaj kisi ka aib chupao. Allah tumhare aib chupayega.",
    "Day 11: Aaj 'Astaghfirullah' 100 baar kaho. Gunah dhul jayenge.",
    "Day 12: Aaj fajr ki namaz ke baad 10 min dua mein guzaro.",
    "Day 13: Aaj hasad ko dil se nikalne ki niyat karo.",
    "Day 14: Aaj 'SubhanAllah wa bihamdihi' 100 baar padho.",
    "Day 15: Aaj kisi roote hue ko hasao. Sadqa hai.",
    "Day 16: Aaj apne nafs se 1 baar 'Nahi' kaho. Koi buri aadat chhodo.",
    "Day 17: Aaj 'Hasbunallahu wa ni'mal wakeel' 7 baar padho.",
    "Day 18: Aaj 2 rakat Salat-ul-Hajat padh ke apni hajat maango.",
    "Day 19: Aaj wazu ki halat mein sone ki koshish karo.",
    "Day 20: Aaj 'Ya Lateefu' 129 baar padho. Mushkil aasan hogi.",
    "Day 21: Aaj kisi se jhooth mat bolo. 1 din ki mashq.",
    "Day 22: Aaj Surah Ikhlas 3 baar padho = 1 Quran ka sawab.",
    "Day 23: Aaj gussa aaye to 'Auzubillah' padh ke khamosh ho jao.",
    "Day 24: Aaj 'Rabbi zidni ilma' 10 baar padho. Ilm badhega.",
    "Day 25: Aaj kisi yateem ke sar pe haath phero ya uske liye dua karo.",
    "Day 26: Aaj 'Inna lillahi wa inna ilayhi raji'un' ka matlab samjho.",
    "Day 27: Aaj 1000 baar 'Allah' kaho. Dil zinda ho jayega.",
    "Day 28: Aaj tahajjud mein uthne ki niyat karke so jao.",
    "Day 29: Aaj 'La ilaha illallah' ki gawahi dil se do.",
    "Day 30: Aaj pichle 29 din ka hisab lo. Kya badla?",
    "Day 31: Aaj 'Ya Wadoodu' 20 baar padh ke mohabbat ki dua karo.",
    "Day 32: Aaj kisi ka qarz utarne ki dua karo, ya apna ada karo.",
    "Day 33: Aaj 'Fabi ayyi ala i rabbikuma tukazziban' pe gaur karo.",
    "Day 34: Aaj poora din shikayat ka 1 lafz bhi na nikle zubaan se.",
    "Day 35: Aaj 'Hasbi Allah' par yaqeen rakho. Wo kaafi hai.",
    "Day 36: Aaj apne walidain ke pairon mein jannat talash karo.",
    "Day 37: Aaj 'Rabbi ishrah li sadri' padh ke kaam shuru karo.",
    "Day 38: Aaj kisi ko pani pilao. Behtareen sadqa hai.",
    "Day 39: Aaj maut ko yaad karo. Zindagi ki qadar hogi.",
    "Day 40: Mubarak! Aaj shukrane ke 2 nafal padho. Safar poora hua."
]

TASBEEH = [
    "1. SubhanAllah 33 baar",
    "2. Alhamdulillah 33 baar",
    "3. Allahu Akbar 34 baar",
    "4. Astaghfirullah 100 baar",
    "5. Durood Shareef 10 baar"
]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    CHAT_IDS.add(chat_id)
    user_name = update.effective_user.first_name

    await update.message.reply_text(
        f"Assalamualaikum {user_name} 🌙\n\n"
        f"40 Din Sakoon ke safar mein khush amadeed.\n\n"
        f"Roz subah 6 baje naya sabaq milega.\n\n"
        f"Commands:\n"
        f"/sabaq - Aaj ka sabaq\n"
        f"/tasbeeh - Aaj ki tasbeeh\n"
        f"/safar - Safar dobara shuru karo"
    )

# /sabaq command
async def sabaq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = len(CHAT_IDS) % 40 # Simple logic. Behtar: DB use karo
    await update.message.reply_text(f"📖 Aaj ka Sabaq:\n\n{SABAQ[day]}")

# /tasbeeh command
async def tasbeeh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasbeeh_text = "\n".join(TASBEEH)
    await update.message.reply_text(f"📿 Aaj ki Tasbeeh:\n\n{tasbeeh_text}\n\nDil se, dhyaan se padhna.")

# /safar command
async def safar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    CHAT_IDS.add(chat_id)
    await update.message.reply_text(
        "Alhamdulillah! Tumhara 40 din ka safar shuru ✅\n\n"
        "Kal subah 6 baje pehla sabaq milega InshaAllah.\n"
        "Sabr, shukr aur istiqamat."
    )

# Daily sabaq bhejne wala function
async def daily_sabaq(context: ContextTypes.DEFAULT_TYPE):
    day = context.job.data
    sabaq_text = SABAQ[day % 40]

    for chat_id in CHAT_IDS:
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"🌅 Subah Bakhair\n📖 Day {day+1} ka Sabaq:\n\n{sabaq_text}\n\n/tasbeeh bhej kar tasbeeh le lena."
            )
        except:
            pass # User ne block kar diya hoga

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sabaq", sabaq))
    app.add_handler(CommandHandler("tasbeeh", tasbeeh))
    app.add_handler(CommandHandler("safar", safar))

    # Roz subah 6 baje India time pe sabaq bhejo
    job_queue = app.job_queue
    job_queue.run_daily(daily_sabaq, time(hour=6, minute=0, tzinfo=pytz.timezone('Asia/Kolkata')), data=0)

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
