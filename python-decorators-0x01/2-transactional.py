import sqlite3
import functools

"""
Objective: 
Create a decorator that manages database transactions by automatically 
committing or rolling back changes

Instructions:
Complete the script below by writing a decorator transactional(func) 
that ensures a function running a database operation is wrapped inside a transaction.
If the function raises an error, rollback; otherwise commit the transaction.

"""

"""your code goes here"""


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        return func(*args, **kwargs)
    return wrapper


def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except sqlite3.Error as e:
            print(f"Transaction Failed: {e}")
            raise
        finally:
            conn.close()
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?",
                   (new_email, user_id))
# Update user's email with automatic transaction handling


update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
