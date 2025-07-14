import os
OWNER_ID = "1872929674"

async def notify_owner(bot, user, respuesta):
    msg = f"🗳️ Nuevo interesado\n👤 Usuario: @{user.username}\n✅ Interés: {respuesta.capitalize()}"
    await bot.send_message(chat_id=OWNER_ID, text=msg)

async def notify_expulsion(bot, username):
    msg = f"❌ Usuario expulsado por inactividad\n👤 Usuario: @{username}\n🕒 Motivo: No compartió archivo en 5 horas"
    await bot.send_message(chat_id=OWNER_ID, text=msg)
