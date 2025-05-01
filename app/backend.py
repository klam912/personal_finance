from flask import Flask, render_template
from markupsafe import escape

# Initialize a Flask instance
app = Flask(__name__)

# Initialize routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/login")
def welcome():
    return render_template('login.html')