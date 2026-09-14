import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade REAL
)
""")
connection.commit()
while True:
    print("=== Student Management System ===")
    print()
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")
    print()
    
    choose = int(input("Enter your choose: "))
    print()
    if choose <1 or choose > 6:
        print("Invalid choose!")
        exit()

    elif choose == 1:
     name = input("Enter student name: ")
     age = int(input("Enter student age: "))
     grade = float(input("Enter student grade: "))
     cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        (name, age, grade)
     )
     connection.commit()
     print("Student added successfully!")

    elif choose == 2:
     cursor.execute("SELECT * FROM students")
     students = cursor.fetchall()
     for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Grade: {student[3]}")
        print()
    elif choose == 3:
       search = input("Enter the name of student you want to search: ")
       cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    (search,)
)
       result =  cursor.fetchone()  
       if result:
          print(f"{search} exist in table!")
       else:
          print(f"{search} doesn't exist in table!")
    elif choose == 4:
       student_id = int(input("Enter student ID: "))
       new_name = input("Enter new name: ")

       cursor.execute(
         "UPDATE students SET name = ? WHERE id = ?",
         (new_name, student_id)
          )
       connection.commit()
       print("Student updated successfully!")
    elif choose == 5:
        delete = input("Entre the id of student you want to delete: ")
        cursor.execute(
           "DELETE FROM students WHERE id = ?",
           (delete,)
        )  
        connection.commit()
        print("You have delete this student successfully")
    elif choose == 6:
       exit()    
      