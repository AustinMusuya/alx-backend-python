#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        user='root',
        password='your_password',  # Replace with your actual root password
        host='localhost',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch  # Yield each batch
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  # Loop #1
        filtered = [user for user in batch if float(user['age']) > 25]  # Loop #2 (implicit)
        yield filtered  # Each batch of users over 25
