import json
import os
from telegram import Bot
from utils.notify import notify_expulsion

DATA_FILE = "activity.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def track_user_activity(user_id):
    data = load_data()
    data[str(user_id)] = {"active": True}
    save_data(data)

async def check_inactive_users(context):
    job_data = context.job.data
    user_id = str(job_data["user_id"])
    chat_id = job_data["chat_id"]
    bot: Bot = context.bot

    data = load_data()
    if user_id not in data or not data[user_id].get("active"):
        await bot.send_message(chat_id, 
            f"El usuario @{job_data['username']} no compartió ningún archivo. Será eliminado.\n"
            f"The user @{job_data['username']} did not share any file and will be removed.")
        await bot.ban_chat_member(chat_id, int(user_id))
        await bot.unban_chat_member(chat_id, int(user_id))
        await notify_expulsion(bot, job_data['username'])
    else:
        del data[user_id]
        save_data(data)
