from validators import validate_email, validate_phone
import database

class Student:

    def __init__(
        self,
        student_id,
        full_name,
        email,
        phone_number,
        date_of_birth,
        department_id,
        level,
        registration_date
    ):
        self.student_id = student_id
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.department_id = department_id
        self.level = level
        self.registration_date = registration_date



def register_student():
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")

    while True:
        email = input("Enter Email: ")

        if validate_email(email):
            break

        print("Invalid email. Please try again.")

    while True:
        phone_number = input("Enter Phone Number: ")

        if validate_phone(phone_number):
            break

        print("Invalid phone number. Please try again.")

    date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
    departments = database.get_departments()

    print("\nAvailable Departments:")

    for department in departments:
        print(f"{department[0]}. {department[1]}")

    department_id = int(input("Enter Department ID: "))
    level = int(input("Enter Level: "))
    registration_date = input("Enter Registration Date (YYYY-MM-DD): ")

    new_student = Student(
        student_id,
        full_name,
        email,
        phone_number,
        date_of_birth,
        department_id,
        level,
        registration_date
    )
    
    database.add_student(new_student)

    return new_student 





def view_students():
    students = database.get_students()

    if not students:
        print("No students found.")
    else:
        print("\n===== STUDENTS =====")

        for student in students:
            print(f"Student ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Email: {student[2]}")
            print(f"Phone: {student[3]}")
            print(f"Date of Birth: {student[4]}")
            print(f"Department ID: {student[5]}")
            print(f"Level: {student[6]}")
            print(f"Registration Date: {student[7]}")
            print("----------------------------")


def search_student():
    student_id = input("Enter Student ID to search: ")

    student = database.find_student_by_id(student_id)

    if student:
        print("\n===== STUDENT DETAILS =====")
        print(f"Student ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Email: {student[2]}")
        print(f"Phone: {student[3]}")
        print(f"Date of Birth: {student[4]}")
        print(f"Department ID: {student[5]}")
        print(f"Level: {student[6]}")
        print(f"Registration Date: {student[7]}")
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    student = database.find_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print("\n===== UPDATE STUDENT =====")
    print("1. Full Name")
    print("2. Email")
    print("3. Phone Number")
    print("4. Date of Birth")
    print("5. Department")
    print("6. Level")
    print("7. Cancel")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_value = input("Enter new full name: ")
        field = "full_name"

    elif choice == "2":
        while True:
            new_value = input("Enter new email: ")

            if validate_email(new_value):
                break

            print("Invalid email. Please try again.")

        field = "email"

    elif choice == "3":
        while True:
            new_value = input("Enter new phone number: ")

            if validate_phone(new_value):
                break

            print("Invalid phone number. Please try again.")    

        field = "phone_number"
        
    
    elif choice == "4":
        new_value = input("Enter new date of birth (YYYY-MM-DD): ")
        field = "date_of_birth"

    elif choice == "5":
        departments = database.get_departments()

        print("\nAvailable Departments:")

        for department in departments:
            print(f"{department[0]}. {department[1]}")

        new_value = int(input("Enter new Department ID: "))
        field = "department_id"

    elif choice == "6":
        new_value = int(input("Enter new level: "))
        field = "level"

    elif choice == "7":
        print("Update cancelled.")
        return

    else:
        print("Invalid choice.")
        return

    database.update_student_field(student_id, field, new_value)

    print("Student updated successfully.")



def delete_student():
    student_id = input("Enter Student ID to delete: ")

    student = database.find_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print("\n===== STUDENT TO DELETE =====")
    print(f"Student ID: {student[0]}")
    print(f"Name: {student[1]}")
    print(f"Email: {student[2]}")

    confirmation = input(
        "Are you sure you want to delete this student? (Y/N): "
    )

    if confirmation.upper() == "Y":
        database.delete_student(student_id)
        print("Student deleted successfully.")

    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n===== UNIVERSITY STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()