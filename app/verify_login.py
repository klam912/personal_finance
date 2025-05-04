import supabase
from flask import current_app
from app.supabase_client import supabase

def verify_login(username, password):    
    res = supabase.table("User").select("*").eq("username", username).eq("password", password).execute()

    return res