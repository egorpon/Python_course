def two_Sum(list,target):
    seen = {}
    i = 0
    for num in list:
        difference = target - num
        if difference in seen:
            return [seen[difference], i]
        seen[num] = i
        i+=1
   



print(two_Sum([3,2,4],6))