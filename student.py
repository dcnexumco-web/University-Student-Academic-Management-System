from validators import validate_email, validate_phone
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

    return new_student