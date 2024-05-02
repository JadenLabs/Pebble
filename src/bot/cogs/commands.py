from discord import Interaction, AppCommandType
from discord.ext.commands import Cog, CheckFailure
from src.bot.bot import Bot
from src.base.config import config
from src.utils.logger import logger
from src.utils.embeds import no_user_perms_embed


class Commands(Cog):
    """Commands Events"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send(embed=no_user_perms_embed)

    @Cog.listener()
    async def on_app_command_completion(
        self, ctx: Interaction, command: AppCommandType
    ):
        logger.info(f"{command.name} done ${ctx.guild.id} @{ctx.user.id}")


async def setup(bot: Bot):
    await bot.add_cog(Commands(bot))
