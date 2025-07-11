import mysql.connector
from dotenv import load_dotenv
import os

"""
Objective: create a reusable context manager that takes a query as input and executes it, 
managing both connection and the query execution

Instructions:
Implement a class based custom context manager ExecuteQuery that takes the query: 
”SELECT * FROM users WHERE age > ?” and the parameter 25 and returns the result of the query
Ensure to use the__enter__() and the __exit__() methods

"""
# Load environment variables
load_dotenv()


class ExecuteQuery():
    def __init__(self, query, params=None):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=os.getenv("user"),
            password=os.getenv("password"),
            database=os.getenv("database")
        )
        self.query = query
        self.params = params or ()

    def __enter__(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor  # Return cursor for executing queries

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()


query = "SELECT * FROM users WHERE age > %s"
params = (25,)

with ExecuteQuery(query, params) as cursor:
    results = cursor.fetchall()
    for row in results:
        print(row)
