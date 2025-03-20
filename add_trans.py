import sqlite3
import set_up_db


def add_transaction(user_input: list):
    # Assign variables from user input
    date = user_input[0]
    trans_type = user_input[1]
    category = user_input[2]
    amount = int(user_input[3])

    # Validate the data types
    if not isinstance(date, str):
        raise TypeError("Date must be a string (format: YYYY-MM-DD).")
    if not isinstance(trans_type, str):
        raise TypeError("Transaction type must be a string (e.g., 'income' or 'expense').")
    if not isinstance(category, str):
        raise TypeError("Category must be a string (e.g., 'groceries' or 'salary').")
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number.")

    # Connect to the database
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    # Add entry to the transaction table
    cursor.execute("""
        INSERT INTO transactions (date, trans_type, category, amount)
        VALUES (?, ?, ?, ?)
    """, (date, trans_type, category, amount))

    conn.commit()
    conn.close()
    print("Transaction added successfully!")



