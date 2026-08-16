import sqlite3


def create_database():
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone_number TEXT NOT NULL UNIQUE,
        date_of_birth TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        level INTEGER NOT NULL,
        registration_date TEXT NOT NULL,

        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_code TEXT PRIMARY KEY,
        course_title TEXT NOT NULL,
        course_unit INTEGER NOT NULL,
        semester TEXT NOT NULL,
        department_id INTEGER NOT NULL,

        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id TEXT,
        course_code TEXT,

        PRIMARY KEY (student_id, course_code),

        FOREIGN KEY (student_id)
        REFERENCES students(student_id),

        FOREIGN KEY (course_code)
        REFERENCES courses(course_code)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        course_code TEXT NOT NULL,
        test_score REAL NOT NULL,
        exam_score REAL NOT NULL,
        total_score REAL NOT NULL,
        grade TEXT NOT NULL,
        grade_point REAL NOT NULL,
        quality_point REAL NOT NULL,

        FOREIGN KEY (student_id)
        REFERENCES students(student_id),

        FOREIGN KEY (course_code)
        REFERENCES courses(course_code)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        course_code TEXT NOT NULL,
        attendance_date TEXT NOT NULL,
        status TEXT NOT NULL,

        FOREIGN KEY (student_id)
        REFERENCES students(student_id),

        FOREIGN KEY (course_code)
        REFERENCES courses(course_code)
    )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()


#STUDENT MANAGEMENT FUNCTIONS
def add_student(student):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students (
        student_id,
        full_name,
        email,
        phone_number,
        date_of_birth,
        department_id,
        level,
        registration_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student.student_id,
        student.full_name,
        student.email,
        student.phone_number,
        student.date_of_birth,
        student.department_id,
        student.level,
        student.registration_date
    ))

    connection.commit()
    connection.close()




def add_department(department_name):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO departments (department_name)
    VALUES (?)
    """, (department_name,))

    connection.commit()
    connection.close()

def get_departments():
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()

    connection.close()
    return departments


def get_students():
    connection = sqlite3.connect('university.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()
    return students


def find_student_by_id(student_id):
    connection = sqlite3.connect('university.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()

    connection.close()
    return student


def update_student_field(student_id, field, new_value):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    query = f"UPDATE students SET {field} = ? WHERE student_id = ?"

    cursor.execute(query, (new_value, student_id))

    connection.commit()
    connection.close()


def delete_student(student_id):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))

    connection.commit()
    connection.close()



#COURSE MANAGEMENT FUNCTIONS

def add_course(course):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO courses (
        course_code,
        course_title,
        course_unit,
        semester,
        department_id
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        course.course_code,
        course.course_title,
        course.course_unit,
        course.semester,
        course.department_id
    ))

    connection.commit()
    connection.close()


def get_courses():
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    connection.close()

    return courses


def find_course_by_code(course_code):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM courses WHERE course_code = ?",
        (course_code,)
    )

    course = cursor.fetchone()

    connection.close()

    return course

def update_course_field(course_code, field, new_value):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    query = f"UPDATE courses SET {field} = ? WHERE course_code = ?"

    cursor.execute(query, (new_value, course_code))

    connection.commit()
    connection.close()


def delete_course(course_code):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM courses WHERE course_code = ?",
        (course_code,)
    )

    connection.commit()
    connection.close()


#RESULT MANAGEMENT FUNCTIONS

def add_result(result):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO results (
            student_id,
            course_code,
            test_score,
            exam_score,
            total_score,
            grade,
            grade_point,
            quality_point
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        result.student_id,
        result.course_code,
        result.test_score,
        result.exam_score,
        result.total_score,
        result.grade,
        result.grade_point,
        result.quality_point
    ))

    connection.commit()
    connection.close()


def get_results():
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM results")
    results = cursor.fetchall()

    connection.close()

    return results


def find_results_by_student_id(student_id):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM results WHERE student_id = ?",
        (student_id,)
    )

    results = cursor.fetchall()

    connection.close()

    return results


def update_result_field(result_id, field, new_value):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    query = f"UPDATE results SET {field} = ? WHERE result_id = ?"

    cursor.execute(query, (new_value, result_id))

    connection.commit()
    connection.close()


def delete_result(result_id):
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM results WHERE result_id = ?",
        (result_id,)
    )

    connection.commit()
    connection.close()