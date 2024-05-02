from discord import app_commands, Interaction, Embed
from discord.ext.commands import Cog
from src.base.config import config
from src.bot.bot import Bot


class Ping(Cog):
    """Ping cog"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pings the pebble")
    async def ping(self, ctx: Interaction):
        """Pings the bot."""
        ping = round(self.bot.latency * 1000)

        embed = Embed(
            color=config.colors["primary"],
            description=f"{config.emojis['network_w']} Pong! `{ping}ms`",
        )

        await ctx.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Ping(bot))
