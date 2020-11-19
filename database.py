"""
    Author: Brett Larson
    Date: 11/04/2020

    Functionality:
        The database.py file provides functions for creating and writing transactions to the credit
        card processing application's database.
"""

# Required Imports
import sqlite3
from datetime import datetime


def create_database_and_tables(database_name):
    """
    This method creates the requested database, and adds one table to it,
    :param database_name: The name of the database to create,
    """

    # Timestamp variable for logging
    timestamp = str(datetime.now())

    try:
        print(timestamp + ': Creating the database specified if one does not already exist.')
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            date text,
                            transaction_guid text,
                            name text,
                            card_number text,
                            exp_date text,
                            zip_code text,
                            purchase_amt real,
                            approval_status text,
                            approval_code text
                            )''')
        conn.commit()
        conn.close()
        print(timestamp + ': The database was created successfully, or it already exists.')

    except sqlite3.OperationalError:
        print(timestamp + ': There was an error attempting to create the table')
        conn.rollback()
        conn.close()


def write_transaction_data(transaction, database_name):
    """
    This function inserts transaction data into the database.
    :param transaction: A dictionary with relevant transaction data.
    :param database_name: The name of the database to write to.
    """

    # Timestamp variable for logging
    timestamp = str(datetime.now())

    sql_insert_string = f"INSERT INTO transactions VALUES ('{transaction['current_date_time']}', " \
                        f"'{transaction['transaction_number']}', '{transaction['name']}', " \
                        f"'{transaction['card_number']}', '{transaction['exp_date']}', " \
                        f"'{transaction['zip_code']}', '{transaction['purchase_amt']}', " \
                        f"'{transaction['approval_status']}', '{transaction['authorization_code']}')"

    try:
        print(timestamp + ': Writing the transaction to the database.')
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(sql_insert_string)
        conn.commit()
        conn.close()
        print(timestamp + ': The transaction was written successfully to the database.')
    except sqlite3.OperationalError:
        print(timestamp + ': There was an error attempting to add data to the database')
        conn.rollback()
        conn.close()
    except sqlite3.IntegrityError:
        print(timestamp + ': Data you are attempting to add is invalid or not formatted properly')
        conn.rollback()
        conn.close()
