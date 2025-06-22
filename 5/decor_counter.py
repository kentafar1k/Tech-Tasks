from functools import wraps


def count_param(n):
    def decorator(func):
        count = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= n:
                raise RuntimeError(f"Превышено колличество вызовов ({n})")
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@count_param(2)
def f1():
    print('nigga')

f1()
f1()
f1()



