from typing import Callable
from functools import wraps
import time


def deco(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end-start}")
        return res
    return wrapper


def some_func(time_sleep):
    time.sleep(time_sleep)
    return "ky"

some_func = deco(some_func)
print(some_func(1))

