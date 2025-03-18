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
            date DATE NOT NULL UNIQUE,
            total_income REAL DEFAULT 0,
            total_spending REAL DEFAULT 0,
            weekday TEXT NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            week INTEGER NOT NULL,
            FOREIGN KEY (date) REFERENCES transactions (date)
        )
    """)

    # Trigger to update daily when a transaction is inserted
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_daily_income_spending
        AFTER INSERT ON transactions
        BEGIN
            -- Insert a new date into daily if it doesn't exist
            INSERT INTO daily (date, weekday, month, year, week)
            VALUES (
                NEW.date,
                strftime('%w', NEW.date),
                strftime('%m', NEW.date),
                strftime('%Y', NEW.date),
                strftime('%W', NEW.date)
            )
            ON CONFLICT(date) DO NOTHING;

            -- Update total_income and total_spending
            UPDATE daily
            SET total_income = (
                SELECT COALESCE(SUM(amount), 0) 
                FROM transactions 
                WHERE transactions.date = daily.date 
                AND transactions.trans_type = 'income'
            ),
            total_spending = (
                SELECT COALESCE(SUM(amount), 0) 
                FROM transactions 
                WHERE transactions.date = daily.date 
                AND transactions.trans_type = 'spending'
            )
            WHERE daily.date = NEW.date;
        END;
    """)


    # Create week table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weekly (
            week INTEGER NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            total_income REAL DEFAULT 0,
            total_spending REAL DEFAULT 0,
            PRIMARY KEY (week, year)
        )
    """)

    # Drop the old trigger if it exists
    cursor.execute("DROP TRIGGER IF EXISTS update_weekly_income_spending")

    # Create a new trigger for INSERT on daily
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_weekly_income_spending_insert
        AFTER INSERT ON daily
        BEGIN
            -- Ensure the week exists in the weekly table
            INSERT INTO weekly (week, month, year)
            VALUES (
                NEW.week, NEW.month, NEW.year
            )
            ON CONFLICT(week, year) DO UPDATE SET
                month = NEW.month;

            -- Update weekly totals
            UPDATE weekly
            SET 
                total_income = (
                    SELECT COALESCE(SUM(total_income), 0) 
                    FROM daily 
                    WHERE daily.week = NEW.week 
                    AND daily.year = NEW.year
                ),
                total_spending = (
                    SELECT COALESCE(SUM(total_spending), 0) 
                    FROM daily 
                    WHERE daily.week = NEW.week 
                    AND daily.year = NEW.year
                )
            WHERE 
                weekly.week = NEW.week 
                AND weekly.year = NEW.year;
        END;
    """)
    
    # Create a separate trigger for UPDATE on daily
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_weekly_income_spending_update
        AFTER UPDATE ON daily
        BEGIN
            -- Update weekly totals when daily is updated
            UPDATE weekly
            SET 
                total_income = (
                    SELECT COALESCE(SUM(total_income), 0) 
                    FROM daily 
                    WHERE daily.week = NEW.week 
                    AND daily.year = NEW.year
                ),
                total_spending = (
                    SELECT COALESCE(SUM(total_spending), 0) 
                    FROM daily 
                    WHERE daily.week = NEW.week 
                    AND daily.year = NEW.year
                )
            WHERE 
                weekly.week = NEW.week 
                AND weekly.year = NEW.year;
        END;
    """)

    # Create month table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monthly (
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            total_income REAL DEFAULT 0,
            total_spending REAL DEFAULT 0,
            PRIMARY KEY (month, year)
        )
    """)

    # Create a trigger for INSERT on weekly
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_monthly_income_spending_insert
        AFTER INSERT ON weekly
        BEGIN
            INSERT INTO monthly (month, year)
            VALUES (NEW.month, NEW.year)
            ON CONFLICT (month, year) DO NOTHING;

            UPDATE monthly
            SET 
                total_income = (
                    SELECT COALESCE(SUM(total_income), 0)
                    FROM weekly
                    WHERE weekly.month = NEW.month AND weekly.year = NEW.year
                ),
                total_spending = (
                    SELECT COALESCE(SUM(total_spending), 0)
                    FROM weekly
                    WHERE weekly.month = NEW.month AND weekly.year = NEW.year   
                )
            WHERE monthly.month = NEW.month AND monthly.year = NEW.year;
        END;
"""
    )

    # Create a trigger for UPDATE on weekly
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_monthly_income_spending_update
        AFTER UPDATE ON weekly
        BEGIN
            UPDATE monthly
            SET 
                total_income = (
                    SELECT COALESCE(SUM(total_income), 0)
                    FROM weekly
                    WHERE weekly.month = NEW.month AND weekly.year = NEW.year
                ),
                total_spending = (
                    SELECT COALESCE(SUM(total_spending), 0)
                    FROM weekly
                    WHERE weekly.month = NEW.month AND weekly.year = NEW.year   
                )
            WHERE monthly.month = NEW.month AND monthly.year = NEW.year;
        END;
"""
    )


    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()