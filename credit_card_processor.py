"""
    Author: Brett Larson
    Date: 11/04/2020

    Description:
        This Python file represents the credit card processing vendor that the credit card app
        server calls to receive an approval or declined message. In this case, approval is based
        on the amount of the purchase.

        This code is based on the week four assignment with additional modifications to integrate
        with the new program features and functionality.
"""

# Required imports
import random
import string
import json


def authorize_transaction(json_data):
    """
    This function represents the credit card vendor. It takes data received from the API server,
    and calls additional functions to approve or decline a transaction. It builds a new JSON
    object to send back to the server.
    :param json_data: Data received from the POST request from the Simple API server.
    :return: JSON object with approval information.
    """

    print('Beginning the authorization workflow.')

    data_dict = json.loads(json_data)
    masked_card_number = mask_credit_card(data_dict)
    approval = approve_deny_transaction(data_dict)

    if approval == 'approve':
        auth_code = get_authorization_code()
        decision_dict = build_approval_dict(approval, auth_code, masked_card_number)
        json_decision = json.dumps(decision_dict)
    elif approval == 'decline':
        auth_code = 0
        decision_dict = build_decline_dict(approval,auth_code, masked_card_number)
        json_decision = json.dumps(decision_dict)

    return json_decision


def approve_deny_transaction(data_dict):
    """
    This function approves transactions with a purchase value of less than or equal to 200 and
    greater than 0.
    :param data_dict: JSON POST data stored in a dictionary
    :return: string "approve" or "decline"
    """

    approval = 'approve'
    amount = float(data_dict.get('purchase_amt'))

    print('Approving or declining the transaction based on the amount.')

    if amount >= 200 or amount < 0:
        approval = 'decline'
    print(f"The transaction is " + approval)

    return approval


def get_authorization_code():
    """
    Create an authorization code through the creation of a string of random letters and numbers
    :return: string authorization code
    """

    print('Creating the authorization code.')

    letters_numbers = string.ascii_letters + string.digits
    authorization_code = ''.join((random.choice(letters_numbers) for i in range(10)))

    print(f"The authorization code is " + authorization_code)

    return authorization_code


def mask_credit_card(data_dict):
    """
    Take the credit card number provided by the user, and truncate it to the last four numbers.
    :param data_dict: Dictionary provided by the customer
    :return: String containing the last four digits of the credit card number
    """

    print('Masking the credit card number.')

    credit_card_num = data_dict.get('card_number')
    last_four_num = credit_card_num[-4:]

    return last_four_num


def build_approval_dict(approval, auth_code, card_num):
    """
    Function that builds the dictionary when a card is approved.
    :param approval: approval status (should always be "approved" for this function)
    :param auth_code: generated authorization code
    :param card_num: Last four digits of the credit card number
    :return: dictionary with approval data
    """

    approval_dict = {"approval_status": approval,
                     "authorization_code": auth_code,
                     "last_four_card_number": card_num}

    return approval_dict


def build_decline_dict(approval,auth_code, card_num):
    """
    Function that builds the dictionary when a card is declined.
    :param auth_code: generated authorization code (0 for declines)
    :param approval: approval status (should always be "decline" for this function)
    :param card_num: Last four digits of the credit card number
    :return: dictionary with decline data
    """

    decline_dict = {"approval_status": approval,
                    "authorization_code": auth_code,
                    "last_four_card_number": card_num}

    return decline_dict
