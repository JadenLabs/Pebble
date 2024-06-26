from discord import app_commands, Interaction, Embed
from discord.ext.commands import Cog
from src.base.config import config
from src.utils.logger import logger
from src.utils import server
from src.bot.bot import Bot


class Dev(Cog):
    """Ping cog"""

    def __init__(self, bot: Bot):
        self.bot = bot

    #     @app_commands.command(name="db_test", description="Dev: test db")
    #     async def db_test(self, ctx: Interaction):
    #         """Dev command for db testing"""
    #         await ctx.response.defer()

    #         user_data = {
    #             "user_id": ctx.user.id,
    #             "username": ctx.user.name,
    #             "global_name": ctx.user.global_name,
    #             "servers": {},
    #         }
    #         logger.debug(f"user_data: {user_data}")

    #         user_db = database.db.users
    #         user_doc_id = user_db.insert_one(user_data).inserted_id

    #         embed = Embed(
    #             color=config.colors["primary"],
    #             description=f"""\
    # > {user_doc_id}

    # ```json
    # {user_data}
    # ```
    # """,
    #         )

    #         await ctx.edit_original_response(embed=embed)

#     @app_commands.command(
#         name="create_server_doc", description="Dev: create server doc"
#     )
#     async def create_server_doc(self, ctx: Interaction):
#         """Dev command to create server doc"""
#         if ctx.user.id != 1027380375028244551:
#             return

#         await ctx.response.defer()

#         server_doc = server.find_or_create(ctx.guild)

#         embed = Embed(
#             color=config.colors["primary"],
#             description=f"""\
# > {server_doc["_id"]}

# ```json
# {server_doc}
# ```
# """,
#         )

#         await ctx.edit_original_response(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Dev(bot))
