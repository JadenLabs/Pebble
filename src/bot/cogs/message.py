from discord import Message, Embed, DMChannel
from discord.ext.commands import Cog, CheckFailure
from src.bot.bot import Bot
from src.base.config import config
from src.utils import user
from src.utils.logger import logger
from src.database.database import database


class Message(Cog):
    """Message Events"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return
        if isinstance(message.channel, DMChannel):
            return

        logger.debug(f"Message create: ${message.guild.id} @{message.author.id}")

        user_doc, user_is_new = user.find_or_create(message)

        await user.handle_msg_xp_event(message)

        logger.debug(f"Finished block from {message.author.id}")


async def setup(bot: Bot):
    await bot.add_cog(Message(bot))
