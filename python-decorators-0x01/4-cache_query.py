import time
import sqlite3
import functools


"""
Objective: create a decorator that caches the results of a database queries 
inorder to avoid redundant calls

Instructions:
Complete the code below by implementing a decorator cache_query(func) 
that caches query results based on the SQL query string

"""

query_cache = {}


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        return func(*args, **kwargs)
    return wrapper


"""your code goes here"""


def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query in query_cache:
            print("[Cache] Returning cached result.")
            return query_cache[query]

        print("[DB] Executing query and caching result.")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
