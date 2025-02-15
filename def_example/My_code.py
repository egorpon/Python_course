def isEven(num):
    return num % 2 == 0


def partition(lst, func):
    truthy_list = []
    falsy_list = []
    for a in lst:
        if func(a):
            truthy_list.append(a)
        else:
            falsy_list.append(a)

    return [truthy_list, falsy_list]


print(partition([1, 2, 3, 4], isEven))  # [[2,4],[1,3]]
print(6 / 2)
