'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
from csv import reader
def find_user(first,last):
    with open("users.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        users = list(csv_reader)
        for row in users:
            if first in row and  last in row:
                    return users.index(row)+1
        return 'Not Here not found.'
        # for user in users:
        #     if user["First Name"] == first and user["Last Name"] == last:
        #         return users.index(user)+1
        # return 'Not Here not found'



print(find_user("Alan", "Turing"))
print(find_user("Colt", "Steele"))
print(find_user("Not", "Here"))
