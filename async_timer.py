import asyncio


async def timer(delay):
    await asyncio.sleep(delay)
    print('Task')

async def main(timers):
    t = [timer(0.5) for _ in range(timers)]
    await asyncio.gather(*t)
    print('Tasks Done')


asyncio.run(main(5))