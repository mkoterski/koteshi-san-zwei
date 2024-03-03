sqltest3.py

import sqlite3

# Path to the SQLite database file
db_path = "/home/matthias/projects/tests/test003 - sensor-read/sensors_database/sensorsData.db"

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a query to retrieve data (you can modify this query as needed)
    query = "SELECT * FROM DHT_data"
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Print the retrieved data
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except sqlite3.Error as e:
    print(f"Error accessing the database: {e}")
