import supabase
from flask import current_app
from app.supabase_client import supabase

def add_entry_user(entry):
    """Add user credentials (in JSON) to the User table"""
    # Insert the entry into User table 
    response = supabase.table("User").insert(entry).execute()
    return response


def add_entry_day(entry):
    """Add income and spending information (in JSON) to the Day table"""
    try:
        response = supabase.table("Day").insert(entry).execute()
        return
    except Exception as e:
        print(f"Failed to add entry: {str(e)}")
        raise e