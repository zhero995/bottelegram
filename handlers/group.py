from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from utils.tracker import track_user_activity, check_inactive_users

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        context.job_queue.run_once(
            check_inactive_users,
            when=18000,
            data={"chat_id": update.effective_chat.id, "user_id": member.id, "username": member.username}
        )
        await update.message.reply_text(
            f"¡Bienvenido {member.full_name}! Tienes 5 horas para subir un archivo STL o serás eliminado.
"
            f"Welcome {member.full_name}! You have 5 hours to upload an STL file or you'll be removed."
        )

async def handle_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    track_user_activity(user_id)

def setup_group_handlers(app):
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_files))
