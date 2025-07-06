#!/usr/bin/python3
import mysql.connector

def stream_users():
    connection = mysql.connector.connect(
        user='root',
        password='warmachine!',  # Replace with your actual password
        host='localhost',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:  # Only one loop, as required
            yield row
    finally:
        cursor.close()
        connection.close()
