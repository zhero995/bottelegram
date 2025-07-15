# Diccionario para llevar control de actividad de usuarios
user_activity = {}

def track_user_activity(user_id):
    user_activity[user_id] = True

def check_inactive_users():
    # Devuelve IDs de usuarios que no han estado activos
    return [user_id for user_id, active in user_activity.items() if not active]
