#!/usr/bin/python3
import mysql.connector


def paginate_users(page_size, offset):
    # Real logic is handled below
    return _paginate_users_with_conn(page_size, offset)

# Internal function that actually uses the connection
def _paginate_users_with_conn(page_size, offset):
    connection = mysql.connector.connect(
        user='root',
        password='warmachine!',
        host='localhost',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

def lazy_paginate(page_size):
    offset = 0
    while True:  # Only one loop
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
