#!/usr/bin/python3
import mysql.connector

def paginate_users(connection, page_size, offset):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset)
        )
        return cursor.fetchall()
    finally:
        cursor.close()

def lazy_paginate(page_size):
    connection = mysql.connector.connect(
        user='root',
        password='your_password',  # Replace with your actual root password
        host='localhost',
        database='ALX_prodev'
    )

    try:
        offset = 0
        while True:  # Single loop
            page = paginate_users(connection, page_size, offset)
            if not page:
                break
            yield page
            offset += page_size
    finally:
        connection.close()
