from supabase import Client, create_client
import os
from dotenv import load_dotenv

# API Docs: https://supabase.com/docs/reference/python/delete

# Load all environment variables from .env
load_dotenv()

# Get creds
API_KEY = os.getenv('API_KEY')
PROJECT_URL = os.getenv("PROJECT_URL")

# Initialize the client
supabase: Client = create_client(PROJECT_URL, API_KEY)

# Create user
new_user = {
    'id': 3,
    'first_name': 'john',
    'last_name': 'doe',
    'email': 'johndoe@gmail.com',
    'username': 'johndoe',
    'password': '1234'
}

# Insert the entry into User table 
response = supabase.table("User").insert(new_user).execute()


