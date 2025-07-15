from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from utils.tracker import track_user_activity

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    track_user_activity(user_id)
    await update.message.reply_text(
        "👥 ¡Bienvenido al grupo!\n"
        "👥 Welcome to the group!"
    )

def setup_group_handlers(app):
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
