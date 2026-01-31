import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

def check_stock(item):
    print(f"Checking {item}")
    time.sleep(3)
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "gold")
        print(result)

asyncio.run(main())