import datetime
import functools


class Decorator:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):  # call позволяет использовать класс как функцию, а здесь как декоратор
        start = datetime.datetime.now()
        result = self.func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"Время выполнения: {end - start}")
        return result






@Decorator
def print_hello():
    """я функция хелло"""
    return 'Hello!'

print(print_hello())
print(print_hello.__doc__)