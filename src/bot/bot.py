import os
from discord import Intents, CustomActivity
from discord.ext.commands import AutoShardedBot
from src.utils.logger import logger
from src.base.config import config
from cogwatch import watch


class Bot(AutoShardedBot):
    """Main bot class"""

    def __init__(self, **options) -> None:
        super().__init__(command_prefix="nb.", intents=Intents.default(), **options)

    async def load_extensions(self):
        """Loads all the extensions / cogs in the ./cogs folder"""
        for f in os.listdir("./src/bot/cogs"):
            if f.endswith(".py"):
                await self.load_extension("src.bot.cogs." + f[:-3])
                logger.info(f"Successfully loaded cog: {f[:-3]}")

    async def start(self):
        """Starts the bot"""
        try:
            logger.info("Starting the bot")
            await super().start(config.token, reconnect=True)
        except Exception as e:
            raise Exception(f"Bot failed to startup: {e}")

    async def setup_hook(self) -> None:
        """Hook for when the bot is being setup, used to load all the extensions"""
        await self.load_extensions()
        await self.tree.sync()

    @watch(path="src/bot/cogs", colors=True)
    async def on_ready(self):
        """Called when the bot is ready"""
        try:
            activity = CustomActivity(config.bot_activity)
            await self.change_presence(status=config.bot_status, activity=activity)
            logger.info("Set status completed")
        except Exception as e:
            logger.error(f"Error setting presence: {e}")

        # Finish
        logger.info("Bot is ready")
