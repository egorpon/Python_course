"""
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
"""


def ensure_fewer_than_three_args(fn):
    def wrapper(a=0, *args, **kwargs):
        if len(args) < 3:
            print("Too many arguments!")
        return fn(args, kwargs)

    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


add_all()  # 0
add_all(1)  # 1
add_all(1, 2)  # 3
add_all(1, 2, 3)  # "Too many arguments!"
add_all(1, 2, 3, 4, 5, 6)  # "Too many arguments!"
