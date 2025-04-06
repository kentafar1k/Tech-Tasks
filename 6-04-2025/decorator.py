from functools import wraps

def decorator_attrs(count_repeat):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """я декоратор"""
            for _ in range(count_repeat):
                func(*args, **kwargs)
        return wrapper
    return decorator






@decorator_attrs(5)
def print_hello():
    """я хелло ворлд"""
    print('Hello World!')

print(print_hello.__doc__)  # без wraps выведет "я декоратор"

print_hello()