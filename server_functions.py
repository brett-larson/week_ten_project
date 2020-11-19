"""
    Author: Brett Larson
    Date: 11/04/2020

    Functionality:
        The server_functions.py file provides various functions to the web server.
"""

# Required Imports
from datetime import datetime

from credit_card_processor import *
from database import *


def approval_process(form_data_dict, json_data):
    """
    Back-end server function that is called from the web server (server.py) to get authorization
    from the processing vendor and store results in the database.
    :param form_data_dict:
    :param json_data:
    :return:
    """

    authorization = json.loads(authorize_transaction(json_data))
    write_to_db(form_data_dict, authorization)

    return authorization


def write_to_db(web_dict, vendor_dict):
    """
    This function allows the server to write data to the database.
    :param web_dict: Dictionary containing customer information
    :param vendor_dict: Dictionary containing vendor provided information
    """

    database_name = 'transactions.db'

    current_date_time = str(datetime.now())
    transaction_number = get_transaction_guid()
    web_dict.update(vendor_dict)
    web_dict['transaction_number'] = transaction_number
    web_dict['current_date_time'] = current_date_time
    write_transaction_data(web_dict, database_name)


def get_transaction_guid():
    """
    This function provides a unique transaction ID (GUID) for each transaction
    :return: Unique string of numbers representing the transaction ID
    """

    numbers = string.digits
    transaction_number = ''.join((random.choice(numbers) for i in range(10)))

    return transaction_number
