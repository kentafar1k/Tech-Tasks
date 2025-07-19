from typing import Callable
from functools import wraps
import time


def deco(func: Callable):
    @wraps(func)
    def wrapper():
        start = time.time()
        res = func()
        end = time.time()
        print(f"Время выполнения: {end-start}")
        return res
    return wrapper


def some_func():
    time.sleep(0.5)
    return "ky"

some_func = deco(some_func)
print(some_func())