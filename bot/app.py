import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7814527305:AAH6m15oC-jnLF9fSabHozup3MRLcZzxMsE"
WEBHOOK_URL = f"https://shchepkov.ru/{TOKEN}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Бот работает в Docker! 🐳')


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Настройка вебхука
    app.run_webhook(
        listen="0.0.0.0",
        port=8443,
        url_path=TOKEN,
        webhook_url=WEBHOOK_URL
    )


if __name__ == '__main__':
    main()