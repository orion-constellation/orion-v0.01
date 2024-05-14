import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('your_database.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Execute the query
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results from the cursor into a list
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()