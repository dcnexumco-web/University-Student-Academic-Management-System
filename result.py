import database


class Result:
    def __init__(
        self,
        student_id,
        course_code,
        test_score,
        exam_score,
        total_score,
        grade,
        grade_point,
        quality_point
    ):
        self.student_id = student_id
        self.course_code = course_code
        self.test_score = test_score
        self.exam_score = exam_score
        self.total_score = total_score
        self.grade = grade
        self.grade_point = grade_point
        self.quality_point = quality_point


def register_result():
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

    try:
        test_score = float(input("Enter Test Score: "))
        exam_score = float(input("Enter Exam Score: "))
    except ValueError:
        print("Invalid score. Please enter a number.")
        return

    if test_score < 0 or test_score > 40:
        print("Test score must be between 0 and 40.")
        return

    if exam_score < 0 or exam_score > 60:
        print("Exam score must be between 0 and 60.")
        return

    total_score = test_score + exam_score

    if total_score >= 70:
        grade = "A"
        grade_point = 5

    elif total_score >= 60:
        grade = "B"
        grade_point = 4

    elif total_score >= 50:
        grade = "C"
        grade_point = 3

    elif total_score >= 45:
        grade = "D"
        grade_point = 2

    elif total_score >= 40:
        grade = "E"
        grade_point = 1

    else:
        grade = "F"
        grade_point = 0

    course_unit = course[2]
    quality_point = grade_point * course_unit

    new_result = Result(
        student_id,
        course_code,
        test_score,
        exam_score,
        total_score,
        grade,
        grade_point,
        quality_point
    )

    database.add_result(new_result)

    print("\nResult registered successfully.")
    print(f"Total Score: {total_score}")
    print(f"Grade: {grade}")
    print(f"Grade Point: {grade_point}")
    print(f"Quality Point: {quality_point}")


def view_results():
    results = database.get_results()

    if not results:
        print("\nNo results found.")
        return

    print("\n===== RESULTS =====")

    for result in results:
        print(f"Result ID: {result[0]}")
        print(f"Student ID: {result[1]}")
        print(f"Course Code: {result[2]}")
        print(f"Test Score: {result[3]}")
        print(f"Exam Score: {result[4]}")
        print(f"Total Score: {result[5]}")
        print(f"Grade: {result[6]}")
        print(f"Grade Point: {result[7]}")
        print(f"Quality Point: {result[8]}")
        print("----------------------------")


def search_result():
    student_id = input("Enter Student ID: ")

    results = database.find_results_by_student_id(student_id)

    if not results:
        print("No results found for this student.")
        return

    print("\n===== STUDENT RESULTS =====")

    for result in results:
        print(f"Result ID: {result[0]}")
        print(f"Student ID: {result[1]}")
        print(f"Course Code: {result[2]}")
        print(f"Test Score: {result[3]}")
        print(f"Exam Score: {result[4]}")
        print(f"Total Score: {result[5]}")
        print(f"Grade: {result[6]}")
        print(f"Grade Point: {result[7]}")
        print(f"Quality Point: {result[8]}")
        print("----------------------------")


def update_result():
    result_id = input("Enter Result ID to update: ")

    results = database.get_results()

    result = None

    for record in results:
        if str(record[0]) == result_id:
            result = record
            break

    if not result:
        print("Result not found.")
        return

    print("\n===== CURRENT RESULT =====")
    print(f"Result ID: {result[0]}")
    print(f"Student ID: {result[1]}")
    print(f"Course Code: {result[2]}")
    print(f"Test Score: {result[3]}")
    print(f"Exam Score: {result[4]}")
    print(f"Total Score: {result[5]}")
    print(f"Grade: {result[6]}")
    print(f"Grade Point: {result[7]}")
    print(f"Quality Point: {result[8]}")

    print("\nWhat do you want to update?")
    print("1. Test Score")
    print("2. Exam Score")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            new_value = float(input("Enter new Test Score: "))

            if new_value < 0 or new_value > 40:
                print("Test score must be between 0 and 40.")
                return

            field = "test_score"

        elif choice == "2":
            new_value = float(input("Enter new Exam Score: "))

            if new_value < 0 or new_value > 60:
                print("Exam score must be between 0 and 60.")
                return

            field = "exam_score"

        else:
            print("Invalid choice.")
            return

    except ValueError:
        print("Invalid score. Please enter a number.")
        return

    database.update_result_field(
        result_id,
        field,
        new_value
    )

    print("Result updated successfully.")


def delete_result():
    result_id = input("Enter Result ID to delete: ")

    results = database.get_results()

    result = None

    for record in results:
        if str(record[0]) == result_id:
            result = record
            break

    if not result:
        print("Result not found.")
        return

    print("\n===== RESULT TO DELETE =====")
    print(f"Result ID: {result[0]}")
    print(f"Student ID: {result[1]}")
    print(f"Course Code: {result[2]}")
    print(f"Total Score: {result[5]}")
    print(f"Grade: {result[6]}")

    confirmation = input(
        "Are you sure you want to delete this result? (Y/N): "
    )

    if confirmation.upper() == "Y":
        database.delete_result(result_id)
        print("Result deleted successfully.")

    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n===== RESULT MANAGEMENT =====")
        print("1. Register Result")
        print("2. View Results")
        print("3. Search Result")
        print("4. Update Result")
        print("5. Delete Result")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_result()

        elif choice == "2":
            view_results()

        elif choice == "3":
            search_result()

        elif choice == "4":
            update_result()

        elif choice == "5":
            delete_result()

        elif choice == "6":
            print("Leaving Result Management...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()