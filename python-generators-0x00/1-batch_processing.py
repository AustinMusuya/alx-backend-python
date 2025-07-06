#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        user='root',
        password='warmachine!',  # Replace with actual password
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
            yield batch
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    total_yielded = 0
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        filtered = [user for user in batch if float(user['age']) > 25]  # Loop 2
        yield filtered
        total_yielded += len(filtered)
    return total_yielded 
