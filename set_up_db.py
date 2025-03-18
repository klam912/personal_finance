import sqlite3

def create_database():
    # Create the database
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    # Create transaction table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            trans_type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)

    # Create daily table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            total_income REAL NOT NULL,
            total_spending REAL NOT NULL,
            weekday TEXT NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            week INTEGER NOT NULL,
            FOREIGN KEY (date) REFERENCES transactions (date)
        )
    """)

    # Create week table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weekly (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week INTEGER NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            total_income REAL NOT NULL,
            total_spending REAL NOT NULL,
            FOREIGN KEY (week) REFERENCES daily (week)
        )
    """)

    # Create month table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monthly (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            total_income REAL NOT NULL,
            total_spending REAL NOT NULL,
            FOREIGN KEY (month, year) REFERENCES daily (month, year)
        )
    """)


    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()