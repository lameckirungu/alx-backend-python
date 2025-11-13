import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect(DB_FILE) as conn:
        cursor = await conn.cursor()
        await cursor.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        return results

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_FILE) as conn:
        cursor = await conn.cursor()
        await cursor.execute("SELECT * FROM users WHERE age > 40")
        results = await cursor.fetchall()
        return results

async def main():
    tasks = [
        async_fetch_users(),
        async_fetch_older_users()
    ]
    
    all_results = await asyncio.gather(*tasks)
    return all_results

if __name__ == "__main__":
    asyncio.run(main())