from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from utils.notify import notify_owner

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    user = update.effective_user
    if lang == "es":
        question = "¿En qué estás interesado?"
        buttons = [
            [InlineKeyboardButton("🖨️ Impresión 3D", callback_data="impresion")],
            [InlineKeyboardButton("💻 Modelado digital", callback_data="modelado")],
            [InlineKeyboardButton("🕹️ Videojuegos", callback_data="videojuegos")],
            [InlineKeyboardButton("👀 Solo explorando", callback_data="explorando")]
        ]
    else:
        question = "What are you interested in?"
        buttons = [
            [InlineKeyboardButton("🖨️ 3D Printing", callback_data="impresion")],
            [InlineKeyboardButton("💻 Digital Modeling", callback_data="modelado")],
            [InlineKeyboardButton("🕹️ Video Games", callback_data="videojuegos")],
            [InlineKeyboardButton("👀 Just exploring", callback_data="explorando")]
        ]
    markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(f"¡Hola {user.first_name}!\n{question}", reply_markup=markup)




async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    await query.answer()
    respuesta = query.data
    await query.edit_message_text(f"¡Gracias! Hemos registrado tu interés: {respuesta.capitalize()}")
    await notify_owner(context.bot, user, respuesta)

def setup_private_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_response))
