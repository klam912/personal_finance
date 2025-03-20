import sqlite3
import set_up_db
import add_trans

def fetch_data(query: str, limit: int):
    # Connect to the database
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    # Execute query
    cursor.execute(query, (limit,))

    # Fetch all results
    rows = cursor.fetchall()

    # Print table
    if rows:
        for row in rows:
            print(row)
    else:
        print("No entries found!")

    conn.close()

def view_transactions(limit: 10):
    trans_query = """
    SELECT *
    FROM transactions
    LIMIT ?
    """
    print("Transactions:")
    fetch_data(trans_query, limit)

def view_daily(limit: 10):
    daily_query = """
    SELECT *
    FROM daily
    LIMIT ?
    """
    print("Daily summary:")
    fetch_data(daily_query, limit)

def view_weekly(limit: 10):
    weekly_query = """
    SELECT *
    FROM weekly
    LIMIT ?
    """
    print("Weekly summary:")
    fetch_data(weekly_query, limit)

def view_monthly(limit: 10):
    monthly_query = """
    SELECT *
    FROM monthly
    LIMIT ?
    """
    print("Monthly summary:")
    fetch_data(monthly_query, limit)