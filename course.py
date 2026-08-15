import database


class Course:
    def __init__(
        self,
        course_code,
        course_title,
        course_unit,
        semester,
        department_id
    ):
        self.course_code = course_code
        self.course_title = course_title
        self.course_unit = course_unit
        self.semester = semester
        self.department_id = department_id



#REGISTER COURSE FUNCTION
def register_course():
    course_code = input("Enter Course Code: ")
    course_title = input("Enter Course Title: ")
    course_unit = int(input("Enter Course Unit: "))
    semester = input("Enter Semester: ")

    departments = database.get_departments()

    print("\nAvailable Departments:")

    for department in departments:
        print(f"{department[0]}. {department[1]}")

    department_id = int(input("Enter Department ID: "))

    new_course = Course(
        course_code,
        course_title,
        course_unit,
        semester,
        department_id
    )

    database.add_course(new_course)

    print("Course registered successfully.")

    return new_course


#VIEW COURSES FUNCTION
def view_courses():
    courses = database.get_courses()

    if not courses:
        print("No courses found.")
        return

    print("\n===== COURSES =====")

    for course in courses:
        print(f"Course Code: {course[0]}")
        print(f"Course Title: {course[1]}")
        print(f"Course Unit: {course[2]}")
        print(f"Semester: {course[3]}")
        print(f"Department ID: {course[4]}")
        print("----------------------------")


#SEARCH COURSE FUNCTION
def search_course():
    course_code = input("Enter Course Code to search: ")

    course = database.find_course_by_code(course_code)

    if course:
        print("\n===== COURSE DETAILS =====")
        print(f"Course Code: {course[0]}")
        print(f"Course Title: {course[1]}")
        print(f"Course Unit: {course[2]}")
        print(f"Semester: {course[3]}")
        print(f"Department ID: {course[4]}")
    else:
        print("Course not found.")


#update course function
def update_course():
    course_code = input("Enter Course Code to update: ")

    course = database.find_course_by_code(course_code)

    if not course:
        print("Course not found.")
        return

    print("\n===== CURRENT COURSE DETAILS =====")
    print(f"Course Code: {course[0]}")
    print(f"Course Title: {course[1]}")
    print(f"Course Unit: {course[2]}")
    print(f"Semester: {course[3]}")
    print(f"Department ID: {course[4]}")

    print("\nWhat do you want to update?")
    print("1. Course Title")
    print("2. Course Unit")
    print("3. Semester")
    print("4. Department")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_value = input("Enter new course title: ")
        field = "course_title"

    elif choice == "2":
        new_value = int(input("Enter new course unit: "))
        field = "course_unit"

    elif choice == "3":
        new_value = input("Enter new semester: ")
        field = "semester"

    elif choice == "4":
        departments = database.get_departments()

        print("\nAvailable Departments:")

        for department in departments:
            print(f"{department[0]}. {department[1]}")

        new_value = int(input("Enter new Department ID: "))
        field = "department_id"

    else:
        print("Invalid choice.")
        return

    database.update_course_field(
        course_code,
        field,
        new_value
    )

    print("Course updated successfully.")



#DELETE COURSE FUNCTION
def delete_course():
    course_code = input("Enter Course Code to delete: ")

    course = database.find_course_by_code(course_code)

    if not course:
        print("Course not found.")
        return

    print("\n===== COURSE TO DELETE =====")
    print(f"Course Code: {course[0]}")
    print(f"Course Title: {course[1]}")
    print(f"Course Unit: {course[2]}")
    print(f"Semester: {course[3]}")

    confirmation = input(
        "Are you sure you want to delete this course? (Y/N): "
    )

    if confirmation.upper() == "Y":
        database.delete_course(course_code)
        print("Course deleted successfully.")

    else:
        print("Deletion cancelled.")


#MAIN FUNCTION0
def main():
    while True:
        print("\n===== COURSE MANAGEMENT =====")
        print("1. Register Course")
        print("2. View Courses")
        print("3. Search Course")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_course()

        elif choice == "2":
            view_courses()

        elif choice == "3":
            search_course()

        elif choice == "4":
            update_course()

        elif choice == "5":
            delete_course()

        elif choice == "6":
            print("Leaving Course Management...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()