import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
class_name TEXT,
department TEXT
)
''')
conn.commit()
conn.close()

# create models
class Student:
    def __init__(self, name, age, class_name, department):
        self.name = name
        self.age = age
        self.class_name = class_name
        self.department = department

    def __str__(self):
           return f"{self.name} | {self.age} | {self.class_name} | {self.department}"


# create database functions

# insert students
def add_students(student):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute('''
INSERT INTO students (name, age, class_name, department)
VALUES
(?, ?, ?, ?)
''', (student.name, student.age, student.class_name, student.department))

    conn.commit()
    conn.close()

# view students in data base 
def view_students():
     conn = sqlite3.connect("school.db")
     cursor = conn.cursor()

     cursor.execute('SELECT * FROM students')
     rows = cursor.fetchall()

     conn.close()
     return rows 

# get a student
def get_student(student_id):
     conn = sqlite3.connect("school.db")
     cursor = conn.cursor()

     cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
     student = cursor.fetchone()
     conn.close()
     return student   

# update student detail

def update_class(student_id, new_class):
     conn = sqlite3.connect("school.db")
     cursor = conn.cursor()

     cursor.execute('''
UPDATE students
SET class_name = ?
WHERE id = ?
''', (new_class, student_id))

     conn.commit()
     conn.close()


#  DELETE student

def delete_student(student_id):
     conn = sqlite3.connect("school.db")
     cursor = conn.cursor()

     cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))

     conn.commit()
     conn.close()


while True:
          print("\n--- SCHOOL MANAGEMENT SYSTEM ---")
          print("1. Add Student")
          print("2. View Students")
          print("3. Update Student Class")
          print("4. Delete Student")
          print("5. Exit")

          choice = input("Select option: ")

          if choice == "1":
               name = input("Full name: ")
               age = input("Age: ")
               class_name = input("Class: ")
               department = input("Department: ")

               student = Student(name, age, class_name, department)
               add_students(student)
               print("Student added successfully")

          elif choice == "2":
               students = view_students()
               for s in students:
                    print (s)     

          elif choice == "3":
               student_id = int(input("Student ID: "))

               student = get_student(student_id)
               if student is None:
                    print("Student not found")
               else:
                    print("Current Record:", student)
                    new_class = input("Enter new class: ")
                    update_class(student_id, new_class)
                    print("Class updated successfully")

          elif choice == "4":
               student_id = int(input("student id: "))

               student = get_student(student_id)
               if student is None:
                    print("Student not found")
               else:
                    print("Student info:", student)
                    confirm = input("Are you sure you want to delete?(yes/no): ")

                    if confirm.lower() == "yes":
                         delete_student(student_id)
                         print("Student deleted")
                    else:
                        print("Delete cancelled") 

          elif choice == "5":
               print("Goodbye")
               break 
          else:
               print("Invalid option")                
                         

               
                        
                            

