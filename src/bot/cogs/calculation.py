import math
from discord import app_commands, Interaction, Embed
from discord.ext.commands import Cog
from src.base.config import config
from src.bot.bot import Bot
from src.utils import calculations as calc


class Calculation(Cog):
    """Calculation cog"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(
        name="xp_for_level", description="Find how much experience you need for a level"
    )
    async def xp_for_level(self, ctx: Interaction, level: int):
        """Find how much experience you need for a level"""
        xp_needed = calc.experience_for_level(level=level, multiplier=200)

        embed = Embed(
            color=config.colors["primary"],
            description=f"{config.emojis['star_w']} You need {xp_needed} xp to reach level {level}.",
        )

        await ctx.response.send_message(embed=embed)

    @app_commands.command(
        name="level_for_xp",
        description="Find what level you would be with an amount of experience",
    )
    async def level_for_xp(self, ctx: Interaction, experience: int):
        """Find what level you would be with an amount of experience"""
        level = math.floor(
            calc.level_for_experience(experience=experience, multiplier=200)
        )

        embed = Embed(
            color=config.colors["primary"],
            description=f"{config.emojis['star_w']} {experience} experience would get you to level {level}.",
        )

        await ctx.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Calculation(bot))
