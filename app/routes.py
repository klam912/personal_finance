from flask import Flask, render_template, request, redirect, url_for, flash
from markupsafe import escape
from app.add_entry import add_entry_user, add_entry_day
from app.verify_login import verify_login
from app.get_info import get_user_id
from app.viz import monthly_summary
from datetime import date

def init_routes(app):
    # Initialize routes
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/user/<username>/dashboard", methods=['POST', 'GET'])
    def dashboard(username):
        if request.method == "POST":
            # Get income and spending information
            income = request.form.get('income-input-dashboard')
            income_category = request.form.get('income-categories')

            spending = request.form.get('spending-input-dashboard')
            spending_category = request.form.get('spending-categories')

            # Get user-id
            user_id = get_user_id(username)

            # Get today's date
            today_date = str(date.today())

            # Create an entry
            day_entry = {
                'user_id': user_id,
                'date': today_date,
                'income': income,
                'income_category': income_category,
                'spending': spending,
                'spending_category': spending_category
            }

            # Add the entry
            add_entry_day(day_entry)

            # Update view
            graphJSON = monthly_summary()

            return render_template('dashboard.html', username=username, graphJSON=graphJSON)

        # GET
        graphJSON = monthly_summary()
        return render_template('dashboard.html', username=username, graphJSON=graphJSON)

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

            add_entry_user(user_creds)

            # Redirect user to login
            return render_template('login.html')
        return render_template('register.html')