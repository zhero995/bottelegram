import os
from telegram.ext import ApplicationBuilder
from handlers.private import setup_private_handlers
from handlers.group import setup_group_handlers

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not TOKEN or not WEBHOOK_URL:
    raise ValueError("Faltan las variables de entorno BOT_TOKEN o WEBHOOK_URL")

app = ApplicationBuilder().token(TOKEN).build()

# Configurar handlers
setup_private_handlers(app)
setup_group_handlers(app)

# Iniciar usando webhook (exclusivo para Railway)
if __name__ == "__main__":
    print("🤖 Bot con Webhook iniciado correctamente en Railway")
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        webhook_url=WEBHOOK_URL
    )
