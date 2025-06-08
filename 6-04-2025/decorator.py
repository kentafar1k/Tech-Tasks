from functools import wraps


def paarams(a):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(a)
            return func(*args, **kwargs)
        return wrapper
    return decorator



@paarams(2)
def return_str():
    """я обычная функция"""
    return "я функция"

print(return_str.__doc__)
print(return_str())
