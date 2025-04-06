class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):  # в обычном синглтоне метод __new__()
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

a = Singleton()
b = Singleton()
print(id(a), id(b))