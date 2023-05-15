import sqlite3

# Connect to a database or create one if it does not exist
conn = sqlite3.connect('example.db')

# Create a table
conn.execute('''CREATE TABLE users
             (id INT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
             age INT NOT NULL);''')

# Get the SQLite version
print("SQLite version:", sqlite3.version)

# Insert data to the table
conn.execute("INSERT INTO users (id, name, age) VALUES (1, 'John', 25)")
conn.execute("INSERT INTO users (id, name, age) VALUES (2, 'Jane', 30)")
conn
