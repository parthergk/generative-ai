import asyncio
import threading

def fun():
    print(f"Logging the system healt")

async def fetch_orders():
    await asyncio.sleep(3)
    print("order fetchd")

asyncio.run(fetch_orders())
threading.Thread(target=fun, daemon=True).start()

