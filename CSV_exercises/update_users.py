from csv import DictReader, DictWriter
def update_users(old_f,old_l,new_f,new_l):
    update = 0
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
    
    for row in users:
        print(row)
    
    with open("users.csv", "w", newline="") as file:
        headers = ["First Name","Last Name"]
        csv_writer = DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for row in users:
            if row["First Name"] == old_f and row ["Last Name"] == old_l:
                # users_list.append(row)
                csv_writer.writerow({"First Name" :new_f,
                                     "Last Name" :new_l,
                                     })
                update+=1
            else:
                csv_writer.writerow(row)
    return f"User updated: {update}"
                



print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.