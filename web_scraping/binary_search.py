def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low<=high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess>item:
            high = mid - 1
        else:
            low = mid + 1


print(binary_search([1,5,8,10,19,21,47],21))