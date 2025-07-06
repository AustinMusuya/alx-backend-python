import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

# 1. Connect to MySQL server (no specific database)
def connect_db():
    try:
        return mysql.connector.connect(
            user='root',
            password='warmachine!',  # TODO: Replace with your actual root password
            host='localhost'
        )
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None

# 2. Create database if it doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("✅ Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"❌ Failed to create database: {err}")
    finally:
        cursor.close()

# 3. Connect specifically to ALX_prodev
def connect_to_prodev():
    try:
        return mysql.connector.connect(
            user='root',
            password='your_password',  # TODO: Replace with your actual root password
            host='localhost',
            database='ALX_prodev'
        )
    except mysql.connector.Error as err:
        print(f"❌ Error connecting to ALX_prodev: {err}")
        return None

# 4. Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        )
        """)
        print("✅ Table user_data created or already exists.")
    except mysql.connector.Error as err:
        print(f"❌ Error creating table: {err}")
    finally:
        cursor.close()

# 5. Insert data from CSV if not already in DB
def insert_data(connection, csv_file):
    cursor = connection.cursor()
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, row['name'], row['email'], row['age']))
        connection.commit()
        print("✅ CSV data inserted successfully.")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        cursor.close()

# 6. Generator to stream one row at a time
def stream_user_data(connection):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    finally:
        cursor.close()
