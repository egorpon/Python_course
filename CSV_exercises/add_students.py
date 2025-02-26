from csv import writer
def add_student(filename, name, group, grade):
    with open(filename,"a",newline="") as file:
        csv_writer = writer(file)
        lst = [name,group,grade]
        csv_writer.writerow(lst)

add_student("students.csv", "David", "8-B", 92)
