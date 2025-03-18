import sqlite3
import set_up_db
import add_trans

def fetch_data(query: str):
    # Connect to the database
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    # Execute query
    cursor.execute(query)

    # Fetch all results
    rows = cursor.fetchall()

    # Print table
    if rows:
        print("Row:")
        for row in rows:
            print(row)
    else:
        print("No entries found!")

    conn.close()

if __name__ == "__main__":
    query = """
    SELECT *
    FROM transactions
"""
    fetch_data(query)