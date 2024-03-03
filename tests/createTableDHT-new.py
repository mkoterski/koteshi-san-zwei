createTableDHT-new.py

import sqlite3

# Path to the SQLite database file
db_path = "/home/matthias/projects/tests/test003 - sensor-read/sensors_database/sensorsData.db"

try:
    # Connect to the database or create a new one
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the provided SQLite commands
    cursor.execute("BEGIN;")
    cursor.execute("CREATE TABLE IF NOT EXISTS DHT_data (timestamp DATETIME, temp NUMERIC, hum NUMERIC);")
    cursor.execute("COMMIT;")

    print("Database and table created successfully!")

    # Close the cursor and connection
    cursor.close()
    conn.close()

except sqlite3.Error as e:
    print(f"Error creating the database: {e}")
