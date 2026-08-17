# University Student Academic Management System

## 1. Project Story and Background

The University Student Academic Management System is a Python-based application developed to manage important student academic information in a university environment.

The project was developed as a practical application of Python programming, Object-Oriented Programming (OOP), database management, and software development concepts.

The system was designed to provide a simple way for administrators to manage students, courses, academic results, attendance records, and generate academic reports from a centralized SQLite database.

Instead of keeping student information, course records, results, and attendance in separate manual records, the system brings these activities together into one application.

---

## 2. Problem Being Solved

Managing student academic information manually can lead to several problems, including:

- Difficulty maintaining accurate student records.
- Duplicate or inconsistent information.
- Difficulty searching for student information.
- Errors when calculating grades and quality points.
- Difficulty tracking student attendance.
- Difficulty generating academic reports.
- Time-consuming record updates and deletions.
- Poor organization of academic data.

This project solves these problems by providing a computerized system that stores and manages academic information using a relational SQLite database.

---

## 3. Project Objectives

The main objectives of the project are to:

- Create a computerized student management system.
- Store student information in a structured database.
- Manage university courses and departments.
- Record and calculate student academic results.
- Calculate grades, grade points, and quality points.
- Track student attendance.
- Allow users to search, update, and delete records.
- Generate student academic reports.
- Demonstrate the use of Python with a relational database.
- Apply Object-Oriented Programming principles in a practical project.

---

## 4. Features

### Student Management

The system allows users to:

- Register new students.
- View registered students.
- Search for students.
- Update student information.
- Delete student records.
- Validate student email and phone information.

### Department Management

The system allows departments to be stored and associated with students and courses.

### Course Management

The system allows users to:

- Register courses.
- View courses.
- Search for courses.
- Update course information.
- Delete courses.
- Associate courses with departments.

### Result Management

The result module allows users to:

- Register student results.
- Enter test and examination scores.
- Calculate total scores.
- Automatically assign grades.
- Calculate grade points.
- Calculate quality points.
- View and manage academic results.
- Update and delete results.

### Attendance Management

The attendance module allows users to:

- Record student attendance.
- Associate attendance with students and courses.
- Record attendance dates.
- Record attendance status.
- View attendance records.
- Update attendance records.
- Delete attendance records.

### Academic Reports

The reporting module allows the system to generate student academic reports containing:

- Student information.
- Course information.
- Scores.
- Grades.
- Grade points.
- Quality points.
- Total course units.
- Total quality points.
- GPA.

---

## 5. Technologies Used

The project was developed using the following technologies:

- **Python** – Main programming language.
- **SQLite** – Relational database management system.
- **SQL** – Used for creating and manipulating database tables.
- **Git/GitHub** – Used for version control and project management.

---

## 6. Python Concepts Demonstrated

The project demonstrates several Python programming concepts, including:

### Variables and Data Types

Used to store student information, scores, course information, attendance records, and other data.

### Conditional Statements

`if`, `elif`, and `else` statements are used for:

- Menu selection.
- Grade calculation.
- Input validation.
- Error handling.

### Loops

`while` and `for` loops are used to:

- Keep menus running.
- Display multiple records.
- Process database results.

### Functions

The system is divided into functions for tasks such as:

- Registering students.
- Searching for students.
- Updating records.
- Deleting records.
- Registering courses.
- Calculating results.
- Generating reports.

### Object-Oriented Programming

Classes such as:

- `Student`
- `Course`
- `Result`
- `Attendance`

are used to represent different entities in the system.

### Exception Handling

`try` and `except` are used to handle errors such as:

- Invalid numeric input.
- Duplicate database records.
- Database integrity errors.

### Modules and Imports

The project is divided into multiple Python modules and uses imports to allow the modules to work together.

### String Formatting

Formatted strings are used to display information clearly to users.

### File and Database Operations

Python's `sqlite3` module is used to connect to and interact with the SQLite database.

---

## 7. Database Structure

The project uses an SQLite database called:

```text
university.db