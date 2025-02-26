import csv

def delete_users(first,last):
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        students = list(csv_reader)
    with open("users.csv","w",newline="") as file:
        headers = ["First Name","Last Name"]
        csv_writer = csv.DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        count = 0
        for row in students:
            if row["First Name"] == first and row["Last Name"] == last:
                count +=1
            else:
                csv_writer.writerow(row)
        return f"Users deleted: {count}."


print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele")) # Users deleted: 2.
print(delete_users("Not", "Here")) # Users deleted: 0.