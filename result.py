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

        test_score = float(input("Enter Test Score: "))
        exam_score = float(input("Enter Exam Score: "))
        exam_score = float(input("Enter Exam Score: "))

        total_score = test_score + exam_score
        total_score = test_score + exam_score