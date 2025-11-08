#!/usr/bin/python3

import mysql.connector
import csv
from mysql.connector import errorcode

DB_HOST = ""
DB_USER = ""
DB_PASSWORD = ""
DB_NAME = "ALX_prodev"

def connect_db():
    try:
        connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def create_database():
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")



def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
        database=DB_NAME
    )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None



def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(5, 2) NOT NULL
        )
        """

    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table user_data already exists.")
        else
            print(f"Failed to create table: {err}")
    

def insert_data(connection, data)
    insert_query = """
    INSERT IGNORE INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """

    try:
        cursor = connection.cursor()
        with open(data, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # Skip the header row

            for row in csv_reader:
                cursor.execute(insert_query, tuple(row))

        connection.commit()
        print("Data inserted successfully.")
        cursor.close()

    except FileNotFoundError:
        print(f"Error: CSV file '{data}' not found.")
    except mysql.connector.Error as err:
        print(f"Failed to insert data: {err}")
        connection.rollback()

