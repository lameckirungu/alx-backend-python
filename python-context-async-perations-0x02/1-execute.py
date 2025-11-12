import sqlite3

# Database connection from task 0
class DatabaseConnection:
    def __init__(self, db_filepath):
        self.filepath = db_filepath
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.filepath)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            if exc_type:
                print("\n[DB] Rolling back changes due to error.")
                self.conn.rollback()
            else:
                self.conn.commit()
                return False # allows any exceptions to propagate
            
            self.conn.close()
            print("Connection closed.")


class ExecuteQuery:

    def __init__(self, query, param, db_filepath):
        self.query = query
        self.param = param
        self.filepath = db_filepath

    def __enter__(self):
        with DatabaseConnection(self.filepath) as conn:
            cursor = conn.cursor()
            cursor.execute(self.query, (self.param,))
            results = cursor.fetchall()
        return results

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Query Execution finished.")
        pass

with ExecuteQuery("SELECT * FROM users WHERE age > ?", 25) as q:
    print(q)
