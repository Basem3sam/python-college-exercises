import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Get user input
name = input("Enter name: ")
grade = float(input("Enter grade: "))

# Insert using parameterized query
cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
conn.commit()

# Display updated table
print("\nUpdated Records:")
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
  print(row)

conn.close()