import sqlite3

# Specify the database path
db_path = "/home/matthias/projects/tests/test003 - sensor-read/sensors_database/sensorsData.db"

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
curs = conn.cursor()

# Create the table if it doesn't exist
curs.execute('''CREATE TABLE IF NOT EXISTS DHT_data
                (timestamp DATETIME, temperature REAL, humidity REAL)''')

# Function to insert data into the table
def add_data(temp, hum):
    curs.execute("INSERT INTO DHT_data VALUES (datetime('now'), ?, ?)", (temp, hum))
    conn.commit()

# Call the function to insert data
add_data(20.5, 30)
add_data(25.8, 40)
add_data(30.3, 50)

# Print the entire database contents
print("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM DHT_data"):
    print(row)

# Close the database after use
conn.close()
