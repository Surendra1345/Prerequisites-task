def chunk_text(text: str):
    for i in range(0, len(text), 800):
        yield text[i:i + 800]


text = "A" * 2000

for chunk in chunk_text(text):
    print(len(chunk))

import asyncio


async def first_operation():
    await asyncio.sleep(4)
    return "First operation completed"


async def second_operation():
    await asyncio.sleep(2)
    return "Second operation completed"


async def third_operation():
    await asyncio.sleep(3)
    return "Third operation completed"

# async def main():
#   results= await asyncio.gather(
#       first_operation(),
#       second_operation(),
#       third_operation() )

#   print(results)

async def main():
    tasks = [
        first_operation(),
        second_operation(),
        third_operation()
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)



asyncio.run(main())

# sequential and asyncio.gather()

import asyncio
from time import perf_counter

async def first_operation():
    await asyncio.sleep(1)
    return "First operation completed"

async def sequential():
    for i in range(20):
        result = await first_operation()
        print(result)

async def concurrent():
    result= await asyncio.gather(*(first_operation() for _ in range(20)))
    print(result)

async def main():
    start = perf_counter()
    await sequential()
    sequential_count=perf_counter()-start
    print(f"Sequential execution time: {sequential_count:.2f} seconds")

    start = perf_counter()
    await concurrent()
    concurrent_count=perf_counter()-start
    print(f"Concurrent execution time: {concurrent_count:.2f} seconds")

    print(f"sequential-concurrent time difference: {sequential_count - concurrent_count:.2f} seconds")

asyncio.run(main())


from functools import lru_cache

@lru_cache
def count_tokens(text: str) -> int:
    return len(text)

text = "Hello, how are you?"
result1=count_tokens(text)
result2=count_tokens(text)
print(f"Token count for '{text}': {result1}")
print(f"Token count for '{text}': {result2}")