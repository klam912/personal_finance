import sqlite3

def clear_db():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION;")
        
        # Delete all records from the transactions table
        cursor.execute("DELETE FROM transactions;")
        
        # Delete all records from the daily and weekly summary tables
        cursor.execute("DELETE FROM daily")
        cursor.execute("DELETE FROM weekly;")
        cursor.execute("DELETE FROM monthly;")
        
        # Reset auto-increment counters
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'transactions';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'daily';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'weekly';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'monthly';")

        # Commit the transaction first before running VACUUM
        conn.commit()
        
        # Run VACUUM outside the transaction
        cursor.execute("VACUUM;")
        print("Database reset successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()