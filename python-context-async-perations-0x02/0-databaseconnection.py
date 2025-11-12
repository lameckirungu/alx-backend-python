import sqlite3

class DatabaseConnection:
    def __init__(self, db_filepath):
        self.filepath = db_filepath
        self.conn = None
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.filepath)
        return self.conn

    def __exit__(self, exc_type, exc_value, trace):
        if exc_type:
            print(f"\n--- Error detected, rolling back changes for {self.filepath}")
            if self.conn:
                self.conn.rollback()
        else:
            if self.conn:
                self.conn.commit()
        if self.conn:
            self.conn.close()
            print("Connection closed.")


with DatabaseConnection(db_name) as conn:
    cursor = conn.cursor()
    conn.execute("SELECT * FROM users") 
    results = cursor.fetchall()

    print("\nQuery Results:")
    print(results)