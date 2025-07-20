from functools import wraps
import asyncio
import random

def retry(exclusions: list, delay: int, max_tries: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            tries = 0
            last_exception = None
            while tries < max_tries:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if type(e) not in exclusions:
                        raise e
                    last_exception = e
                    tries += 1
                    if tries < max_tries:
                        await asyncio.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(exclusions=[TimeoutError, IOError], delay=0.5, max_tries=5)
async def some_func(attempt: int):
    # С 50% вероятностью выбросим исключение
    if random.random() < 0.5:
        raise TimeoutError(f"Timeout on attempt {attempt}")
    return f"Success on attempt {attempt}"

async def main():
    for i in range(6):
        try:
            result = await some_func(i)
            print(result)
        except Exception as e:
            print(f"Failed after retries: {e}")

asyncio.run(main())