from discord import app_commands, Interaction, Embed
from discord.ext.commands import Cog
from src.base.config import config
from src.bot.bot import Bot


class Admin(Cog):
    """Admin cog"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(name="settings", description="Manage your pebble settings")
    async def settings(self, ctx: Interaction):
        """Pebble settings"""
        embed = Embed(
            color=config.colors["primary"],
            description=f"""\
Welcome to the pebble settings, {ctx.user.mention}.
Currently managing `{ctx.guild.name}`.

{config.emojis["arrow_rw"]} Grace: `na`
{config.emojis["arrow_rw"]} Slope: `na`
""",
        )

        await ctx.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Admin(bot))
