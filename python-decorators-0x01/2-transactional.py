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

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)

        except Exception as e:
            conn.rollback()
            print(f"Transaction failed, rolling back. Error: {e}")
            raise e
        else:
            print("Transaction successful, committing..")
            conn.commit()
            return result
        return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

    #### Update user's email with automatic transaction handling

    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')