from discord import app_commands, Interaction, Embed
from discord.ext.commands import Cog
from src.base.config import config
from src.utils import user
from src.utils.logger import logger
from src.bot.bot import Bot


class Levels(Cog):
    """Levels cog"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(
        name="me", description=f"Check your personal profile for {config.bot_name}"
    )
    async def me(self, ctx: Interaction):
        """Command for a user to view their profile"""
        await ctx.response.defer(ephemeral=True)

        user_doc, _ = user.find_or_create(ctx)

        embed = Embed(
            color=config.colors["primary"],
            description=f"""\
Hello {ctx.user.mention}, welcome to your {config.bot_name} profile!

{config.emojis['up_trend_w']} Global Level: `{user_doc['level']}`
{config.emojis['star_w']} Global XP: `{user_doc['total_xp']}`
{config.emojis['chat_w']} Messages: `{user_doc['total_messages']}`
{config.emojis['dns_w']} Servers: `{len(user_doc['servers'].keys())}`
""",
        ).set_footer(text=f"This profile shows your global data for {config.bot_name}.")

        await ctx.edit_original_response(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Levels(bot))
