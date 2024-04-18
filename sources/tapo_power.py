__author__ = "Eolus87"

# Standard libraries
import platform
import asyncio

# Third party libraries
from tapo import ApiClient

# Custom libraries

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def power_reading(target_ip: str, user_name: str, password: str) -> float:
    # Set up the client and connect to the device
    client = ApiClient(user_name, password)
    device = await client.p110(target_ip)

    # Measure the current power
    current_power = await device.get_current_power()
    current_power_float = float(current_power.to_dict()['power'])

    # Clean up
    del client, device

    return current_power_float
