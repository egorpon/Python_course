# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper


def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()

    return wrapper


@shout
def greet(name):
    return f"Hi, I am {name}."


@shout
def order(main, side):
    return f"Hi, I would like the {main}, with a side of {side}, please."


@shout
def lol():
    return "LoL"


print(greet("egor"))
print(order(side="burger", main="fries"))
print(lol())
