import sqlite3
import os

# Define the database file path
db_path = "my_database.db"

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
''')

# Functions
def add_user(name, email, password):
    try:
        query = 'INSERT INTO users (name, email, password) VALUES (?, ?, ?);'
        cursor.execute(query, (name, email, password))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")  # e.g., email already exists

def find_user(email, password=None):
    if password:
        query = "SELECT * FROM users WHERE email = ? AND password = ?"
        cursor.execute(query, (email, password))
    else:
        query = "SELECT * FROM users WHERE email = ?"
        cursor.execute(query, (email,))
    
    return cursor.fetchall()
