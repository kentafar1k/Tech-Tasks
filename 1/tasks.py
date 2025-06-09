

s = ["h", "i", "!"]

def reverse_string(s):
    return s[::-1]

print(reverse_string(s))


# 2 Написать декоратор, который перед вызовом пишет Покупайте наших котиков # 3 добавить аргументы
def params(arg):
    def decorator(func):
        def wrapper():
            print(f"Покупайте наших {arg}!")
            func()
        return wrapper
    return decorator

@params('собачек')
def my_func():
    print('hi')

my_func()