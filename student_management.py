# Student Management System

students = []


# Function to add a student
def add_student():
    student_id = input("Enter Student ID: ")
 # Check if ID already exists
    for student in students:
        if student["ID"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
         "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")


# Function to view all students
def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n========== Student Records ==========")

    for student in students:
        print(f"ID     : {student['ID']}")
        print(f"Name   : {student['Name']}")
        print(f"Age    : {student['Age']}")
        print(f"Course : {student['Course']}")
        print(f"Marks  : {student['Marks']}")
        print("-------------------------------------")

# Function to search for a student
def search_student():
    search_value = input("Enter Student ID or Name: ")

    found = False

    for student in students:
        if (student["ID"] == search_value or
                student["Name"].lower() == search_value.lower()):

            print("\nStudent Found!")
            print(f"ID     : {student['ID']}")
            print(f"Name   : {student['Name']}")
            print(f"Age    : {student['Age']}")
            print(f"Course : {student['Course']}")
            print(f"Marks  : {student['Marks']}")

            found = True
    if not found:
        print("Student not found.")


# Function to update student details
def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == student_id:

            print("\nLeave input blank if you don't want to change it.")

            name = input(f"Enter Name [{student['Name']}]: ")
            age = input(f"Enter Age [{student['Age']}]: ")
            course = input(f"Enter Course [{student['Course']}]: ")
            marks = input(f"Enter Marks [{student['Marks']}]: ")

            if name:
                student["Name"] = name
            if age:
                student["Age"] = int(age)
            if course:
                student["Course"] = course
            if marks:
                student["Marks"] = float(marks)

            print("Student details updated successfully!")
            return
    print("Student not found.")


# Function to delete a student
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

# Main menu
while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("===============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice; Please try again.")