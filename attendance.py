import database

class Attendance:
    def __init__(
        self,
        student_id,
        course_code,
        attendance_date,
        status
    ):
        self.student_id = student_id
        self.course_code = course_code
        self.attendance_date = attendance_date
        self.status = status

def mark_attendance():
    student_id = input("Enter Student ID: ")

    student = database.find_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    course_code = input("Enter Course Code: ")

    course = database.find_course_by_code(course_code)

    if not course:
        print("Course not found.")
        return

    attendance_date = input("Enter Attendance Date (YYYY-MM-DD): ")

    status = input("Enter Status (Present/Absent): ")

    status = status.capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid status.")
        return

    new_attendance = Attendance(
        student_id,
        course_code,
        attendance_date,
        status
    )

    database.add_attendance(new_attendance)

    print("Attendance marked successfully.")