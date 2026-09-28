import sqlite3

conn = sqlite3.connect("Student.db")
cursor = conn.cursor()

# Creating a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
email TEXT UNIQUE
)
''')
conn.commit()

# inserting details into the table

cursor.execute('''
INSERT INTO students(name, age, email)
VALUES (?, ?, ?)
''', ("john", 21, "johnisaac306@gmail.com"))
conn.commit()

# Updationg details from the table

cursor.execute('''
UPDATE students
SET age = ?
WHERE id = ?
''', (21, 1))
conn.commit()

# deleting a specific record
cursor.execute("DELETE FROM students WHERE id = ?", (1,))
conn.commit()

# delete all records
cursor.execute("DELETE FROM students")
conn.commit()

