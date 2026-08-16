import database


def student_academic_report():
    student_id = input("Enter Student ID: ")

    student = database.find_student_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    results = database.find_results_by_student_id(student_id)

    if not results:
        print("No academic results found for this student.")
        return

    print("\n===== STUDENT ACADEMIC REPORT =====")
    print(f"Student ID: {student[0]}")
    print(f"Name: {student[1]}")
    print(f"Email: {student[2]}")
    print(f"Phone: {student[3]}")
    print(f"Department ID: {student[5]}")
    print(f"Level: {student[6]}")

    print("\n===== RESULTS =====")

    total_quality_points = 0
    total_course_units = 0

    for result in results:
        course_code = result[2]
        total_score = result[5]
        grade = result[6]
        grade_point = result[7]
        quality_point = result[8]

        course = database.find_course_by_code(course_code)

        if course:
            course_title = course[1]
            course_unit = course[2]
        else:
            course_title = "Unknown"
            course_unit = 0

        print(f"\nCourse Code: {course_code}")
        print(f"Course Title: {course_title}")
        print(f"Course Unit: {course_unit}")
        print(f"Total Score: {total_score}")
        print(f"Grade: {grade}")
        print(f"Grade Point: {grade_point}")
        print(f"Quality Point: {quality_point}")

        print("----------------------------")

        total_quality_points += quality_point
        total_course_units += course_unit

    if total_course_units > 0:
        gpa = total_quality_points / total_course_units
    else:
        gpa = 0

    print("\n===== GPA =====")
    print(f"Total Quality Points: {total_quality_points}")
    print(f"Total Course Units: {total_course_units}")
    print(f"GPA: {gpa:.2f}")


def main():
    while True:
        print("\n===== REPORT MANAGEMENT =====")
        print("1. Student Academic Report")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_academic_report()

        elif choice == "2":
            print("Leaving Report Management...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()