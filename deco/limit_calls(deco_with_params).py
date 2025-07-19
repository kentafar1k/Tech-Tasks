from typing import Callable
from functools import wraps
import time


def limit_calls(limit: int):
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal limit
            if not limit:
                return f"а всё"
            res = func(*args, **kwargs)
            limit -= 1
            return res
        return inner
    return wrapper

@limit_calls(3)
def some_func():
    return ('ky')

print(some_func())
print(some_func())
print(some_func())
print(some_func())
print(some_func())

# some_func = limit_calls(3)(some_func)