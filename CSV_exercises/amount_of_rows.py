from csv import reader

def count_rows(file):
    with open(file) as f:
        csv_reader = reader(f)
        next(csv_reader)
        return sum(1 for _ in csv_reader)
print(count_rows("people.csv"))
