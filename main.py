import student
import course
import result
import attendance
import report


def main():
    while True:
        print("\n===== UNIVERSITY STUDENT ACADEMIC MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Result Management")
        print("4. Attendance Management")
        print("5. Report Management")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student.main()

        elif choice == "2":
            course.main()

        elif choice == "3":
            result.main()

        elif choice == "4":
            attendance.main()

        elif choice == "5":
            report.main()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()