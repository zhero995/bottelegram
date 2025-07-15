from telegram import Update, ChatMember
from telegram.constants import ChatMemberStatus
from telegram.ext import ContextTypes, MessageHandler, filters
from utils.tracker import track_user_activity, check_inactive_users

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        print(f"✅ CHAT ID: {update.effective_chat.id}")  # 👈 Aquí obtendrás el chat ID real en logs
        context.job_queue.run_once(
            check_inactive_users,
            when=18000,
            data={"chat_id": update.effective_chat.id, "user_id": member.id, "username": member.username}
        )
        await update.message.reply_text(
            f"¡Bienvenido {member.full_name}! Tienes 5 horas para subir un archivo STL o serás eliminado.\n"
            f"Welcome {member.full_name}! You have 5 hours to upload an STL file or you'll be removed."
        )

async def handle_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    track_user_activity(user_id)

async def mention_everyone(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.data["chat_id"]
    bot = context.bot
    try:
        mentions = []
        async for member in bot.get_chat_administrators(chat_id):
            pass  # Solo para iniciar el generador

        async for member in bot.get_chat_members(chat_id):
            if member.status != ChatMemberStatus.LEFT and not member.user.is_bot:
                if member.user.username:
                    mentions.append(f"@{member.user.username}")
                else:
                    mentions.append(member.user.first_name)

        message = "🔔 ¡Recuerden subir sus archivos STL esta semana!\n📦 Todos los aportes son bienvenidos.\n\n"
        message += " ".join(mentions[:30])
        await bot.send_message(chat_id=chat_id, text=message)

    except Exception as e:
        print("Error al mencionar miembros:", e)

def setup_group_handlers(app):
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_files))

    app.job_queue.run_repeating(
        mention_everyone,
        interval=2 * 24 * 60 * 60,
        first=10,
        data={"chat_id": -1000000000000}  # Reemplaza esto después con el ID real del grupo
    )
