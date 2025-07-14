import os
from telegram.ext import ApplicationBuilder
from handlers.private import setup_private_handlers
from handlers.group import setup_group_handlers

TOKEN = "8189855146:AAH9h7RfWawHqC3ytacP361WjfcA5KN4g3Y"

app = ApplicationBuilder().token(TOKEN).build()

setup_private_handlers(app)
setup_group_handlers(app)

print("🤖 Bot iniciado correctamente")
app.run_polling()
