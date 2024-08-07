import pandas as pd
import sqlite3

# Read data from CSV file
csv_file = 'student_data.csv'
df = pd.read_csv(csv_file)

# Print DataFrame columns to verify
print("DataFrame columns:", df.columns)

# Connect to SQLite database
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Drop the STUDENT table if it exists
cursor.execute('DROP TABLE IF EXISTS STUDENT')

# Create the STUDENT table with the correct schema
cursor.execute('''
CREATE TABLE STUDENT (
    name TEXT,
    student_class TEXT,
    section TEXT,
    marks INTEGER
)
''')

# Insert data from DataFrame to SQLite
for row in df.itertuples(index=False):
    # Access columns using the correct names
    print(f"Inserting: {row.name}, {row.student_class}, {row.section}, {row.marks}")
    
    cursor.execute('''
    INSERT INTO STUDENT (name, student_class, section, marks) VALUES (?, ?, ?, ?)
    ''', (row.name, row.student_class, row.section, row.marks))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully from CSV to SQLite.")
