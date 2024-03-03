  GNU nano 5.4                                                                              writerandomdatatodb.py                                                                                        
import sqlite3
from datetime import datetime

# Path to the SQLite database file
db_path = "/home/matthias/projects/tests/test003 - sensor-read/sensors_database/sensorsData.db"

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the INSERT command
    current_time = datetime.now().isoformat()
    temperature = 20.5
    humidity = 30
    cursor.execute("INSERT INTO DHT_data VALUES (?, ?, ?)", (current_time, temperature, humidity))
    conn.commit()

    print(f"Data inserted successfully into the DHT_data table at {current_time}.")
except sqlite3.Error as e:
    print(f"Error: {e}")
finally:
    # Close the database connection
    conn.close()
