import csv

def remove_student(filename,name):
    # students_list = []
    with open(filename) as file:
        csv_reader = csv.DictReader(file)
        students = list(csv_reader)
    with open(filename,"w",newline="") as file:
        headers = ["Name","Group","Grade"]
        csv_writer = csv.DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for student in students:
            if student["Name"] == name:
                continue
            else:
                csv_writer.writerow(student)
            




remove_student(r"CSV_exercises\students.csv", "John")
