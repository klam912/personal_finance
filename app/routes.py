from flask import Flask, render_template, request, redirect, url_for, flash
from markupsafe import escape
from app.add_entry import add_entry
from app.verify_login import verify_login

def init_routes(app):
    # Initialize routes
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/user/<username>/dashboard")
    def dashboard(username):
        return render_template('dashboard.html', username=username)

    @app.route("/login", methods=['POST', 'GET'])
    def login():
        if request.method == "POST":
            # Get username and password
            username = request.form.get('user-name')
            password = request.form.get('password')

            # Query that checks if the username and password exists in the database
            # If so, redirect to /user/{user-name}/dashboard.html
            # If not, alert("You don't have an account")
            res = verify_login(username, password)
            
            # Verify login detail
            if res.data and len(res.data) > 0:
                # Redirect to /username/<username>/dashboard.html
                return redirect(url_for('dashboard', username=username))
            else:
                flash("Invalid login")
                return render_template('login.html')
        return render_template('login.html')

    @app.route("/register", methods=['POST', 'GET'])
    def register():
        if request.method == "POST":
            # Get all of the creds
            first_name = request.form.get('first-name-register')
            last_name = request.form.get('last-name-register')
            email = request.form.get('email-register')
            username = request.form.get('user-name-register')
            password = request.form.get('password-register')

            # Create a JSON
            user_creds = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'username': username,
                'password': password
            }

            # Add user info to database
            add_entry(user_creds)

            # Redirect user to login
            return render_template('login.html')
        return render_template('register.html')