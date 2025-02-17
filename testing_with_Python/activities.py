from random import choice
def eat(food, is_healty):
    if not isinstance(is_healty,bool):
        raise ValueError("is_healthy must be a boolean") 
    ending = "because YOLO!"
    if is_healty:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I didn't mean to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after {num_hours} hour nap"


def is_funny(person):
    if person == "tim":
        return False
    return True

def laugh():
    return choice(('lol','haha', 'tehehe'))
