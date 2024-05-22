from discord import app_commands, Interaction, Embed
from discord.ext.commands import Cog
from src.base.config import config
from src.bot.bot import Bot


class Admin(Cog):
    """Admin cog"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(name="settings", description=f"Manage your {config.bot_name} settings")
    async def settings(self, ctx: Interaction):
        """Bot settings"""
        embed = Embed(
            color=config.colors["primary"],
            description=f"""\
Welcome to the {config.bot_name} settings, {ctx.user.mention}.
Currently managing `{ctx.guild.name}`.

{config.emojis["arrow_rw"]} Grace: `na`
{config.emojis["arrow_rw"]} Slope: `na`
""",
        )

        await ctx.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Admin(bot))
