__author__ = "Eolus87"

# Standard libraries
import platform
import asyncio

# Third party libraries
from tapo import ApiClient

# Custom libraries

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def turn_on(target_ip: str, user_name: str, password: str) -> None:
    client = ApiClient(user_name, password)
    device = await client.p110(target_ip)
    await device.on()


async def turn_off(target_ip: str, user_name: str, password: str) -> None:
    client = ApiClient(user_name, password)
    device = await client.p110(target_ip)
    await device.off()
