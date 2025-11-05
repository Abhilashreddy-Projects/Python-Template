import student.Student as Student
'''
Create a student service, which creates and prints data related to students
A student objet contains these attributes id(numeric), name(string), marks(dictionary {course:marks})
Create a method which takes list of students as input, and prints student name  with highest marks from each course
'''
def execute():
    student1= Student.Student(1, "Abhi", {"Maths":68,"Science":98,"Language":78})
    student2= Student.Student(2, "Anu", {"Maths":90,"Science":34,"Language":45})
    students = [student1, student2]
    for student in students:
         print(f"{student.id} - {student.name}")

execute()