# оптимизировать

import random


def foo(i: int) -> str:
    if random.randrange(3) > 0:
        raise Exception(f'oops {i}')
    return f"magic result {i}"


def call():
    '''call foo 5 times with i =0,1,2,.... First success should print the result otherwise raise Exception.'''
    try:
        print(foo(0))
    except Exception:
        try:
            print(foo(1))
        except Exception:
            try:
                print(foo(2))
            except Exception:
                try:
                    print(foo(3))
                except Exception:
                    try:
                        print(foo(4))
                    except Exception:
                        raise Exception("error") from None


# def call():
call()