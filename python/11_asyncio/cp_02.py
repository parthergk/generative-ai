import asyncio

async def cook(name):
    print(f"cooking {name}...")
    await asyncio.sleep(3)
    print(f"cooked {name}")

async def main():
    await asyncio.gather(
        cook("eggs"),
        cook("chican"),
        cook("tomato")
    )

asyncio.run(main())