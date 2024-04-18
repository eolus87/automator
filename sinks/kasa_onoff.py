__author__ = "Eolus87"

# Standard libraries
import platform
import asyncio

# Third party libraries
import kasa

# Custom libraries

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def turn_on(target_ip: str) -> None:
    plug = kasa.SmartPlug(target_ip)
    await plug.update()
    await plug.turn_on()
    del plug


async def turn_off(target_ip: str) -> None:
    plug = kasa.SmartPlug(target_ip)
    await plug.update()
    await plug.turn_off()
    del plug
