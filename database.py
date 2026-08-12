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


