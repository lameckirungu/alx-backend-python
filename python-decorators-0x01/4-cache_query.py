import time
import sqlite3
import functools

def with_db_connection(func):
    """Decorator that handles opening and closing the database connection"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        try:
            conn = sqlite3.connect('user_db')
            result = func(conn, *args, **kwargs)
            return result
        
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
            
        finally:
            if conn:
                conn.close()
    return wrapper

query_cache = {}

def cache_query(func):
    functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query_string = ""
        if 'query' in kwargs:
            query_string = kwargs['query']
        elif args:
            query_string = args[0]
        else:
            return func(conn, *args, **kwargs)
        
        if query_string in query_cache:
            print(f"Fetching from cache: {query_string}")
            return query_cache[query_string]
        else:
            print(f"Fetching from database: {query_string}")
            result = func(conn, *args, **kwargs)
            query_cache[query_string] = result
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")