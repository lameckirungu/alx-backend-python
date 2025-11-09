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

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(conn, *args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        print("All retries failed.")
                        raise e
                    print(f"Waiting {delay}s before trying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)