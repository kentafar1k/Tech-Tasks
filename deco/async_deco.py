from typing import Coroutine
import asyncio


def deco(coroutine: Coroutine):
    async def wrapper(*args, **kwargs):
        res = await coroutine(*args, **kwargs)
        return res
    return wrapper

@deco
async def some_func():
    await asyncio.sleep(0.5)
    return ('ky')

print(asyncio.run(some_func()))

# some_func = deco(some_func)