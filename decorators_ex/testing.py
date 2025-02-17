# let's define a speed_test decoratar
from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        results = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing: {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return results

    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(90_000_000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(90_000_000)])


print(sum_nums_gen())
print(sum_nums_list())
