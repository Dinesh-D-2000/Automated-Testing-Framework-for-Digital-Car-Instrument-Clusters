import sqlite3

# Define a function to create a connection and cursor
def get_connection():
    conn = sqlite3.connect(r'D:\Automation_testing\test_lib\icons.db')
    cursor = conn.cursor()
    return conn, cursor

# Create a table named 'icons' if it doesn't exist
def create_table():
    conn, cursor = get_connection()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS icons (
            name TEXT NOT NULL,
            image BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def execute_sql_file(file_path):
    conn, cursor = get_connection()
    with open(file_path, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

# Ensure the table is created when the module is imported
create_table()