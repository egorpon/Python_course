from csv import DictReader

def filter_by_pos(file,pos):
    with open(file) as file:
        csv_reader = DictReader(file)
        employee  = list(csv_reader)
        found = False
        for row in employee:
            if row["Position"] == pos:
                print(row)
                found =True
        if not found:
            return "Not found"

filter_by_pos("employees.csv", "Developer")
