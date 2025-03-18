import sqlite3
import set_up_db


def add_transaction(date: str, trans_type: str, category: str, amount: float):
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


if __name__ == "__main__":
    add_transaction("2025-03-17", "income", "salary", 320)
    add_transaction("2025-03-18", "income", "salary", 450)
    add_transaction("2025-03-17", "income", "zelle", 50)
    add_transaction("2025-03-18", "income", "zelle", 10)
    add_transaction("2025-04-18", "income", "zelle", 340)
