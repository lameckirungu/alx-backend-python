#!/usr/bin/python3
# A generator function to stream users from the database
import mysql.connector

seed = __import__('seed')

def stream_users():
    # Managing resources
    connection = None
    cursor = None

    try: 
        connection = seed.connect_to_prodev()

        if not connection:
            return
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    