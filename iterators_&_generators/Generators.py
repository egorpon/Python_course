# def count_up_to(max):
#   count = 1
#   while count <= max:
#     yield count
#     count +=1


# counter = count_up_to(10)
# next(counter)
# for num in counter:
#   print(num)


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        if answer == "yes":
            answer = "no"
        else:
            answer = "yes"


gen = yes_or_no()
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
print(next(gen))  # 'no'
