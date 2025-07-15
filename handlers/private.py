from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 ¡Hola! Este bot está activo y funcionando correctamente.\n"
        "👋 Hello! This bot is up and running successfully."
    )

def setup_private_handlers(app):
    app.add_handler(CommandHandler("start", start))
