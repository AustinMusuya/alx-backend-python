import mysql.connector
import os
from dotenv import load_dotenv

"""

Objective: create a class based context manager to handle 
opening and closing database connections automatically.

Instructions:
Write a class custom context manager DatabaseConnection 
using the __enter__ and the __exit__ methods
Use the context manager with the with statement to be able to perform 
the query SELECT * FROM users. Print the results from the query.

"""

load_dotenv()


class DatabaseConnection():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=os.getenv("user"),
            password=os.getenv("password"),
            database=os.getenv("database")
        )

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor  # Return cursor for executing queries

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()


with DatabaseConnection() as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)
