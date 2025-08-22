import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    "except mysql.connector.Error":
        print(f"Error connecting to MySQL: {Error}")
        
    finally:
        # Close database connection safely
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
