from flask import Flask
from app.add_entry import add_entry_user
from app.routes import init_routes
from app.supabase_client import supabase

def create_app():
    app = Flask(__name__)

    # Add routes
    init_routes(app)
    return app