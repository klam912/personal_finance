import supabase
from app.supabase_client import supabase
from flask import current_app

def get_user_id(username :str):
    """Get the user_id from the User table given the username"""
    res = supabase.table('User').select('id').eq('username', username).execute()

    return res.data[0]['id']