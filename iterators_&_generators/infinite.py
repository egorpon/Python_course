# def current_beat():
#   max = 100
#   nums =(1,2,3,4)
#   i = 0
#   result = []
#   while len(result) < max:
#     if i >= len(nums): i = 0
#     result.append(nums[i])
#     i+=1
#   return result

# print(current_beat())


def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1


counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# def play_kick_dram():
#   if current_beat() ==1:
#     play_sound()
