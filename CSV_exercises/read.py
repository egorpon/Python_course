# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#       each row is a list
#         print(f"{fighter[0]} is from {fighter[1]}")

# Ryu is from Japan
# Ken is from USA
# Chun-Li is from China
# Guile is from USA
# E. Honda is from Japan
# Dhalsim is from India
# Blanka is from Brazil
# Zangief is from Russia




# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)
# [['Name', 'Country', 'Height (in cm)'], ['Ryu', 'Japan', '175'], ['Ken', 'USA', '175'], ['Chun-Li', 'China', '165'], ['Guile', 'USA', '182'], ['E. Honda', 'Japan', '185'], ['Dhalsim', 'India', '176'], ['Blanka', 'Brazil', '192'], ['Zangief', 'Russia', '214']]

from csv import DictReader
with open("fighters.csv") as file:
    cvs_reader = DictReader(file)
    for row in cvs_reader:
        # Each row is an OrderedDict 
        print(row["Name"])
