__author__ = "Eolus87"

# Standard libraries
import platform
import asyncio

# Third party libraries
from tapo import ApiClient

# Custom libraries

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def turn_on_async(target_ip: str, user_name: str, password: str) -> None:
    client = ApiClient(user_name, password)
    device = await client.p100(target_ip)
    await device.on()
    del client
    del device

def turn_on(target_ip: str, user_name: str, password: str) -> None:
    asyncio.run(turn_on_async(target_ip, user_name, password))

async def turn_off_async(target_ip: str, user_name: str, password: str) -> None:
    client = ApiClient(user_name, password)
    device = await client.p100(target_ip)
    await device.off()
    del client
    del device

def turn_off(target_ip: str, user_name: str, password: str) -> None:
    asyncio.run(turn_off_async(target_ip, user_name, password))
