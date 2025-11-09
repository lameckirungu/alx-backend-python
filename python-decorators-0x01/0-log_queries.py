import sqlite3
import functools

#### decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query_arg = ""
        if 'query' in kwargs:
            query_arg = kwargs['query']
        elif args:
            query_arg = args[0]
        print(f"Executing Query: {query_arg}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
print("Fetching users...")
users = fetch_all_users(query="SELECT * FROM users")
print(f"Found users: {users}")