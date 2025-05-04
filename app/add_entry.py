import supabase
from flask import current_app
from app.supabase_client import supabase

def add_entry(entry):
    """Add user credentials (in JSON) to the User table"""
    # Insert the entry into User table 
    response = supabase.table("User").insert(entry).execute()
    return response


