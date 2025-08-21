# YooBee College Management System & Temperature Analysis

## Week 2 - Temperature Analysis
This activity calculates the **average, highest, and lowest temperatures** from a list of temperature values.

---

## Week 3 - Yoobee College Management System
This activity is a **command-line application** built using **SQLite3** to manage student and course information for YooBee College.

### Features
- Students can:
  - Input **name, age, email, phone, date, and address** to register.
  - View the list of registered students.
  - Delete a student by selecting their **student ID**.
- Additional entities such as **Courses, Lecturers, Classes, Enrollments, Assessments, and Results** can also be managed.
- **Results Table**:
  - Used to view the scores students achieved after assignments are approved by lecturers.
  - Grades are then stored and displayed in the results table.

---

## Project Structure
- **db.py** → Handles database connection and `create_tables` function.
- **main.py** → Provides the menu for user choices (add, view, update, delete).
- **yoobee.py** → Implements insert, view, update, and delete functions for all entities.

---

## Database Schema
The relational schema is represented in the file:  
📌 `RelationalSchema_YooBee.png`

---

## Getting Started
### Prerequisites
- Python 3.x installed on your system
- SQLite3 (bundled with Python)

### Running the Project
1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Run the program with:
   ```bash
   python main.py
