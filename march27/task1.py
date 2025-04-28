import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        'https://api.example.com/data1',
        'https://api.example.com/data2',
        'https://api.example.com/data3',
    ]

    results = []

    for url in urls:
        data = await fetch_data(url)
        results.append(data)

    print(results)


# решение

import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        'https://api.example.com/data1',
        'https://api.example.com/data2',
        'https://api.example.com/data3',
    ]

    tasks = [fetch_data(url) for url in urls]

    results = await asyncio.gather(tasks)

    print(results)


asyncio.run(main())