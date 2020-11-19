# ICT4310 Week 10 Assignment
This repository contains the code associated with the Week 10 assignment. The program creates a website for customer to use to enter their credit card information to make a purchase.

## Requirements
The application was developed using the [PyCharm IDE](https://www.jetbrains.com/pycharm/).The application utilizes the following Python libraries:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Cryptography](https://pypi.org/project/cryptography/)
 
Additionally, the project utilizes a basic SQLite database for storing transactions. Please note that the database is not secure, and it is not advidable to use actual credit card information when testing and running the application.

## How to Run the Program
Download the code from the repository, and ensure the following files and folders remain in the directory:
- templates folder
- server.py
- server_functions.py
- database.py
- forms.py
- credit_card_processor.py

Ensure Python and the primary dependencies are installed on your PC, and complete the following steps (Windows):
- Open Windows PowerShell (this may need to be as an admin depending on local PC settings)
- Change the directory in PowerShell to the directory where the code is stored
- Type python server.py + Enter to run the server
- Open a web browser and navigate to https://127.0.0.1:4000

Once the webpage loads, you can submit credit card information for processing.
