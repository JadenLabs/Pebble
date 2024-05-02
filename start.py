import asyncio
from src.bot.bot import Bot
from src.base.config import config
from src.utils.logger import logger

bot = Bot()


async def start():
    logger.info("Starting Process")
    try:
        await bot.start()
    except asyncio.CancelledError:
        logger.warn("Asyncio CancelledError: stopping process...")
        await bot.close()


try:
    asyncio.run(start())
except KeyboardInterrupt:
    pass
