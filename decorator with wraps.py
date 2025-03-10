from functools import wraps


def dec(max_calls):
    def func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Я декоратор"""
            result = None
            for _ in range(max_calls):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return func

@dec(3)
def say_hello():
    """Я функция Hello world"""
    print('Hello World!')

print(say_hello.__doc__)

