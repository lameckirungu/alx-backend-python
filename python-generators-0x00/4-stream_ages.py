#!/usr/bin/python3

seed = __import__('seed')

def stream_user_ages():

    connection = None
    cursor = None

    try:
        connection = seed.connect_to_prodev()
        if not connection:
            return
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield row['age']
        
        
    except Exception as err:
        print(f"Error in generator: {err}")
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()

def calculate_avg():
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average}")
    else:
        print("No users found.")