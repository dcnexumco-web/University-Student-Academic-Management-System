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


def view_attendance():
    attendance_records = database.get_attendance()

    if not attendance_records:
        print("\nNo attendance records found.")
        return

    print("\n===== ATTENDANCE RECORDS =====")

    for attendance in attendance_records:
        print(f"Attendance ID: {attendance[0]}")
        print(f"Student ID: {attendance[1]}")
        print(f"Course Code: {attendance[2]}")
        print(f"Date: {attendance[3]}")
        print(f"Status: {attendance[4]}")
        print("----------------------------")


def search_attendance():
    student_id = input("Enter Student ID: ")

    attendance_records = database.find_attendance_by_student_id(
        student_id
    )

    if not attendance_records:
        print("No attendance records found for this student.")
        return

    print("\n===== STUDENT ATTENDANCE =====")

    for attendance in attendance_records:
        print(f"Attendance ID: {attendance[0]}")
        print(f"Student ID: {attendance[1]}")
        print(f"Course Code: {attendance[2]}")
        print(f"Date: {attendance[3]}")
        print(f"Status: {attendance[4]}")
        print("----------------------------")


def update_attendance():
    attendance_id = input("Enter Attendance ID to update: ")

    attendance_records = database.get_attendance()

    attendance = None

    for record in attendance_records:
        if str(record[0]) == attendance_id:
            attendance = record
            break

    if not attendance:
        print("Attendance record not found.")
        return

    print("\n===== CURRENT ATTENDANCE =====")
    print(f"Attendance ID: {attendance[0]}")
    print(f"Student ID: {attendance[1]}")
    print(f"Course Code: {attendance[2]}")
    print(f"Date: {attendance[3]}")
    print(f"Status: {attendance[4]}")

    print("\nWhat do you want to update?")
    print("1. Attendance Date")
    print("2. Status")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_value = input(
            "Enter new Attendance Date (YYYY-MM-DD): "
        )
        field = "attendance_date"

    elif choice == "2":
        new_value = input(
            "Enter new Status (Present/Absent): "
        )
        new_value = new_value.capitalize()

        if new_value not in ["Present", "Absent"]:
            print("Invalid status.")
            return

        field = "status"

    else:
        print("Invalid choice.")
        return

    database.update_attendance_field(
        attendance_id,
        field,
        new_value
    )

    print("Attendance updated successfully.")


def delete_attendance():
    attendance_id = input("Enter Attendance ID to delete: ")

    attendance_records = database.get_attendance()

    attendance = None

    for record in attendance_records:
        if str(record[0]) == attendance_id:
            attendance = record
            break

    if not attendance:
        print("Attendance record not found.")
        return

    print("\n===== ATTENDANCE TO DELETE =====")
    print(f"Attendance ID: {attendance[0]}")
    print(f"Student ID: {attendance[1]}")
    print(f"Course Code: {attendance[2]}")
    print(f"Date: {attendance[3]}")
    print(f"Status: {attendance[4]}")

    confirmation = input(
        "Are you sure you want to delete this record? (Y/N): "
    )

    if confirmation.upper() == "Y":
        database.delete_attendance(attendance_id)
        print("Attendance deleted successfully.")

    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n===== ATTENDANCE MANAGEMENT =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Search Attendance")
        print("4. Update Attendance")
        print("5. Delete Attendance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            search_attendance()

        elif choice == "4":
            update_attendance()

        elif choice == "5":
            delete_attendance()

        elif choice == "6":
            print("Leaving Attendance Management...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()