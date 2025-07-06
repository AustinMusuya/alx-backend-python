#!/usr/bin/python3
import mysql.connector
from decimal import Decimal

def stream_user_ages():
    connection = mysql.connector.connect(
        user='root',
        password='warmachine!',  # Replace with your actual password
        host='localhost',
        database='ALX_prodev'
    )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT age FROM user_data")
        for (age,) in cursor:  # Loop 1
            yield Decimal(age)
    finally:
        cursor.close()
        connection.close()

def compute_average_age():
    total = Decimal(0)
    count = 0
    for age in stream_user_ages():  # Loop 2
        total += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")
