# def add(a,b):
#     """
#     >>> add(2,3)
#     5
#     >>> add(100,200)
#     300
#     """
#     return a + b


def double(values):
    """
    double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
            ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]


def say_hi():
    """
    >>> say_hi()
    'hi'
    """
    return "hi"


def true_that():
    """
    >>> true_that()
    True
    """
    return True


def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'a': True, 'b': True}
    """
    return {key: True for key in keys}


def compact(collection):
    """
    >>> compact([0,1,2,"",[], False, {}, None, "All done"])
    [1, 2, 'All done']
    """

    lst = []
    for a in collection:
        if a:
            lst.append(a)
    return lst


def isEven(num):
    return num % 2 == 0


def partition(lst, func):
    """
    >>> partition([1,2,3,4], isEven)
    [[2, 4], [1, 3]]
    """
    truthy = []
    falsy = []
    for a in lst:
        if func(a):
            truthy.append(a)
        else:
            falsy.append(a)
    return [truthy, falsy]


# partition([1,2,3,4], isEven) # [[2,4],[1,3]]


def intersection(a, b):
    """
    >>> intersection([1,2,3],[2,3,4])
    [2, 3]

    >>> intersection(['a','b','z'],['x','y','z'])
    ['z']
    """
    return list(set(a).intersection(set(b)))
