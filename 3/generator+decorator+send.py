def decorator(func):
    def wrapper(*args):
        gen = func(*args)
        next(gen)
        return gen
    return wrapper

@decorator
def gen():
    x = yield
    yield x * 2

g = gen()
print(g.send(5)) #
