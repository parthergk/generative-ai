import asyncio

async def cook():
    print(f"cooking...")
    await asyncio.sleep(2)
    print("cooked")

asyncio.run(cook())