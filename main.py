import asyncio
import aiohttp

from classes.bot import MadBot
from config import settings

async def main():
    bot = MadBot(
        token=settings.token,
        session=aiohttp.ClientSession(),
        prefix=settings.prefix
    )
    bot.setup_hook()
    await bot.start()

asyncio.run(main())
