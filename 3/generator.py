def inner():
    yield from (i * 2 for i in [1, 2, 3, 4])
    yield "Done"

def outer():
    yield "Start"
    yield from inner()
    yield "End"

print(list(outer()))

import asyncio

async def s(a, b):
    await asyncio.sleep(a)
    print(b)

async def main():
    await s(1, 'hello')
    await s(2, 'nigga')

asyncio.run(main())
