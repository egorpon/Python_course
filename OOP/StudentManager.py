from statistics import mean as avg


class Student:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.grades = []

    def __repr__(self):
        return f"{self.first} {self.last}"

    def add_grade(self, grade):
        self.grades.append(grade)

    def list_grades(self):
        return self.grades

    def get_average(self):
        return avg(self.grades) if self.grades else 0


class StudentManager:
    def __init__(self):
        self.students_data_base = []

    def add_student(self, student):
        self.students_data_base.append(student)

    def remove_student(self, first, last):
        for student in self.students_data_base:
            if (first.lower() == student.first.lower()) and (
                last.lower() == student.last.lower()
            ):
                self.students_data_base.remove(student)
                print(f"{student} was removed.")
                return
        raise ValueError(f"Student {student} not found")

    def find_student(self, first, last):
        for student in self.students_data_base:
            if (first.lower() == student.first.lower()) and (
                last.lower() == student.last.lower()
            ):
                return student
        raise ValueError(f"Can't find a student {first} {last}")

    def list_students(self):
        if not self.students_data_base:
            return "No students in the data base"
        return self.students_data_base


student1 = Student("John", "Doe", 20)
student1.add_grade(90)
student1.add_grade(78)
student1.add_grade(85)
student1.add_grade(61)

student2 = Student("Jane", "Smith", 22)
student2.add_grade(90)
student2.add_grade(78)

print(student1.list_grades())
print(student2.list_grades())


manager = StudentManager()
manager.add_student(student1)
manager.add_student(student2)

print(manager.list_students())
print(manager.find_student("Jane", "Smith"))
print(student1.get_average())


manager.remove_student("John", "Doe")

print(manager.list_students())
