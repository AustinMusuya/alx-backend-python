"""
Objective: Run multiple database queries concurrently using asyncio.gather.

Instructions:
Use the aiosqlite library to interact with SQLite asynchronously. 
To learn more about it, click here.

Write two asynchronous functions: 
async_fetch_users() and async_fetch_older_users() 
that fetches all users and users older than 40 respectively.

Use the asyncio.gather() to execute both queries concurrently.

Use asyncio.run(fetch_concurrently()) to run the concurrent fetch

"""

import asyncio
import aiosqlite


async def async_fetch_users():  # async function to fetch all users from sqlite db
    db = await aiosqlite.connect("users.db")
    cursor = await db.execute('SELECT * FROM users')
    rows = await cursor.fetchall()

    return rows


async def async_fetch_older_users():  # async function to fetch all users older than 40 from sqlite db
    db = await aiosqlite.connect("users.db")
    query = 'SELECT * FROM users WHERE age > ?'
    val = (40,)
    cursor = await db.execute(query, val)
    rows = await cursor.fetchall()

    return rows


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users(),
    )

asyncio.run(fetch_concurrently())
