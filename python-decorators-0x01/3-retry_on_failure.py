import time
import sqlite3
import functools

"""
Objective: 
Create a decorator that retries database operations 
if they fail due to transient errors

Instructions:
Complete the script below by implementing a retry_on_failure(retries=3, delay=2)
decorator that retries the function of a certain number of times if it raises an exception

"""

# paste your with_db_decorator here


def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        return func(*args, **kwargs)
    return wrapper


""" your code goes here"""


def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            count = 0  # keep track of retry attempts

            while count <= retries:
                try:
                    result = func(conn, *args, **kwargs)
                    conn.commit()
                    return result
                except sqlite3.Error as e:
                    print(f"Transaction Failed: {e}")
                    print(f"Retrying... {count + 1} out of {retries}")
                    count += 1
                    if count > retries:
                        print("Max retries exceeded.")
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# attempt to fetch users with automatic retry on failure


users = fetch_users_with_retry()
print(users)
