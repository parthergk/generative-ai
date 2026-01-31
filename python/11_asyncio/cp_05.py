from concurrent.futures import ProcessPoolExecutor
import asyncio

def enc(data):
    return f"encripted {data}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, enc, "password")
        print (result)

if __name__ == "__main__":
    asyncio.run(main())