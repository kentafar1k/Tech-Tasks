from functools import wraps


def decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        key = str(args)
        if cache.get(key):
            return cache[key]
    return wrapper

@decorator
def f1(word):
    print(word)

f1('nigga')
f1('nigga')
f1('nigorrrr')
