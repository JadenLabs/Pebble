from discord import Message, Embed
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

        logger.debug(f"Message create: ${message.guild.id} @{message.author.id}")

        user_doc, user_is_new = user.find_or_create(message)

        if user_is_new:
            disclaimer_embed = Embed(
                color=config.colors["primary"],
                description=f"Hello {message.author.mention}, sorry to slide into your DMs like this. To respect your privacy, I'd like to let you know the following:\n>>> {config.messages['disclaimer']}",
            ).set_footer(
                text="There shouldn't be another dm from me in the future, so sleep tight."
            )
            await message.author.send(embed=disclaimer_embed)

        await user.handle_msg_xp_event(message)

        logger.debug(f"Finished block from {message.author.id}")


async def setup(bot: Bot):
    await bot.add_cog(Message(bot))
