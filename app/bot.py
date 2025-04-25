from telegram import Bot
from telegram.ext import ApplicationBuilder
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DOMAIN = os.getenv("DOMAIN")  # example.com

bot = Bot(token=TOKEN)
WEBHOOK_URL = f"https://{DOMAIN}/webhook"

async def handle_message(update, context):
    await update.message.reply_text("Привет от FastAPI + Telegram Bot!")