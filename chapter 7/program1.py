import sqlite3

# Create database and table
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Insert 3 students
students = [
  ('Ali', 85.5),
  ('Sara', 92.0),
  ('Mohamed', 78.3)
]

cursor.executemany('INSERT INTO students (name, grade) VALUES (?, ?)', students)
conn.commit()

# Retrieve and print all records
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(row)

conn.close()