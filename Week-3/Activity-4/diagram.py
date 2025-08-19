
# from graphviz import Digraph


# def create_eer():
#     eer = Digraph("EER_YooBee", format="png")
#     eer.attr(rankdir="LR", size="8")

#     entities = {
#         "Student": ["StudentID (PK)", "FirstName", "LastName", "DOB", "Email", "Phone", "Address", "ProgramEnrolled", "DateJoined"],
#         "Lecturer": ["LecturerID (PK)", "FirstName", "LastName", "Email", "Phone", "Specialization", "Department"],
#         "Course": ["CourseID (PK)", "CourseName", "Credits", "Department", "Description"],
#         "Class": ["ClassID (PK)", "CourseID (FK)", "LecturerID (FK)", "Room", "ScheduleDate", "Time"],
#         "Enrollment": ["EnrollmentID (PK)", "StudentID (FK)", "CourseID (FK)", "EnrollmentDate"],
#         "Assessment": ["AssessmentID (PK)", "CourseID (FK)", "AssessmentName", "Weightage", "DueDate"],
#         "Result": ["ResultID (PK)", "AssessmentID (FK)", "StudentID (FK)", "MarksObtained", "Grade"]
#     }

#     for entity, attrs in entities.items():
#         label = f"<<B>{entity}</B><BR/>" + "<BR ALIGN='LEFT'/>".join(attrs) + ">"
#         eer.node(entity, label=label, shape="record")

#     # Relationships
#     eer.edge("Student", "Enrollment", label="1..*")
#     eer.edge("Course", "Enrollment", label="1..*")
#     eer.edge("Lecturer", "Course", label="1..*")
#     eer.edge("Course", "Class", label="1..*")
#     eer.edge("Course", "Assessment", label="1..*")
#     eer.edge("Student", "Result", label="1..*")
#     eer.edge("Assessment", "Result", label="1..*")

#     eer.render("EER_YooBee", cleanup=True)
#     print("✅ EER Diagram saved as EER_YooBee.png")

# def create_schema():
#     schema = Digraph("RelationalSchema_YooBee", format="png")
#     schema.attr(rankdir="LR", size="8")

#     tables = {
#         "Students": ["StudentID (PK)", "FirstName", "LastName", "DOB", "Email", "Phone", "Address", "ProgramEnrolled", "DateJoined"],
#         "Lecturers": ["LecturerID (PK)", "FirstName", "LastName", "Email", "Phone", "Specialization", "Department"],
#         "Courses": ["CourseID (PK)", "CourseName", "Credits", "Department", "Description"],
#         "Classes": ["ClassID (PK)", "CourseID (FK)", "LecturerID (FK)", "Room", "ScheduleDate", "Time"],
#         "Enrollments": ["EnrollmentID (PK)", "StudentID (FK)", "CourseID (FK)", "EnrollmentDate"],
#         "Assessments": ["AssessmentID (PK)", "CourseID (FK)", "AssessmentName", "Weightage", "DueDate"],
#         "Results": ["ResultID (PK)", "AssessmentID (FK)", "StudentID (FK)", "MarksObtained", "Grade"]
#     }

#     for table, cols in tables.items():
#         label = f"<<B>{table}</B><BR ALIGN='LEFT'/>" + "<BR ALIGN='LEFT'/>".join(cols) + ">"
#         schema.node(table, label=label, shape="record")

#     # FK relationships
#     schema.edge("Students", "Enrollments", label="StudentID")
#     schema.edge("Courses", "Enrollments", label="CourseID")
#     schema.edge("Lecturers", "Classes", label="LecturerID")
#     schema.edge("Courses", "Classes", label="CourseID")
#     schema.edge("Courses", "Assessments", label="CourseID")
#     schema.edge("Students", "Results", label="StudentID")
#     schema.edge("Assessments", "Results", label="AssessmentID")

#     schema.render("RelationalSchema_YooBee", cleanup=True)
#     print("✅ Relational Schema Diagram saved as RelationalSchema_YooBee.png")

# if __name__ == "__main__":
#     create_eer()
#     create_schema()
