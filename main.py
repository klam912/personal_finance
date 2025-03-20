import sqlite3
from set_up_db import *
from add_trans import *
from remove_trans import *
from query import *

def main():
    # Create database
    create_database()

    # Add transactions
    user_input = input("Enter transaction (i.e. YYYY-MM-DD, trans_type, category, amount): ")
    transaction_entry = [item.strip() for item in user_input.split(',')]
    add_transaction(transaction_entry)

    # # Query 
    view_transactions(10)
    view_daily(10)
    view_weekly(10)
    view_monthly(10)

    # Clear db (optional)
    # clear_db()



if __name__ == '__main__':
    main()