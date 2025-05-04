from supabase import Client, create_client
import os
from dotenv import load_dotenv

# Load all environment variables from .env
load_dotenv()

# Get creds
API_KEY = os.getenv('API_KEY')
PROJECT_URL = os.getenv("PROJECT_URL")

# Initialize the client
supabase: Client = create_client(PROJECT_URL, API_KEY)