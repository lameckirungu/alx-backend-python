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

@with_db_connection
def get_user_by_id(conn, user_id):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

#### Fetch user by ID with automatic connection handling

user = get_user_by_id(user_id=1)
print(user)