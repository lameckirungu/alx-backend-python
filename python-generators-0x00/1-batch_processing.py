#!/usr/bin/python3
import mysql.connector

seed = __import__('seed')

def stream_users_in_batches(batch_size):
    connection = None
    cursor = None

    try:
        connection = seed.connect_to_prodev()

        if not connection:
            return
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        batch = []

        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch: # edge case: eg if last batch doesn't fill 50
            yield batch
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)