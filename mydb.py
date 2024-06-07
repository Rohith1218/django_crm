import psycopg2
from psycopg2 import sql

# Database connection parameters
host = 'localhost'
user = 'postgres'
password = '1234'
database = 'elderco'

# Initialize variables
conn = None
cursor = None

try:
    # Connect to the default database (usually 'postgres')
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database='postgres'  # Use 'postgres' as a placeholder to create a new DB
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Create a new database
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(database)
    ))
    
    print("Database 'elderco' created successfully.")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
