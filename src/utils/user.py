import math
import random
import traceback
from discord import Interaction, Message
from src.database.database import database
from src.base.config import config
from src.utils.logger import logger
import src.utils.calculations as calc


def find_or_create(ctx: Interaction | Message) -> list[dict, bool]:
    try:
        user = ctx.user if ctx.user else ctx.author
    except AttributeError:
        user = ctx.author

    user_db = database.db.users
    user_doc = user_db.find_one({"user_id": user.id})
    logger.debug(f"Running doc check for @{user.id}")
    user_is_new = False

    if not user_doc:
        user_is_new = True
        user_data = {
            "user_id": user.id,
            "username": user.name,
            "global_name": user.global_name,
            "total_messages": 0,
            "total_xp": 0,
            "level": 0,
            "ping": False,
            "last_message": None,
            "servers": {},
        }
        # logger.debug(f"user_data: {user_data}")
        user_db.insert_one(user_data)
        user_doc = user_db.find_one({"user_id": user.id})
        logger.debug(f"Doc check for @{user.id} failed, made new one")

    return user_doc, user_is_new


async def handle_msg_xp_event(message: Message):
    try:
        # logger.debug("Handling message XP event")

        # Get user doc
        user_db = database.db.users
        user_doc = user_db.find_one({"user_id": message.author.id})

        # * Update global values
        updated_doc = {}
        updated_doc["servers"] = user_doc["servers"]
        updated_doc["total_messages"] = user_doc["total_messages"] + 1
        gained_xp = 200
        updated_doc["total_xp"] = user_doc["total_xp"] + gained_xp

        # Get old and new levels
        old_level = user_doc["level"]
        new_level = math.floor(calc.level_for_experience(updated_doc["total_xp"], 200))
        # print(old_level, new_level)

        if old_level < new_level:
            updated_doc["level"] = new_level
            logger.info(
                f"[global] {message.author.name} has leveled up to level {new_level}"
            )

        # * Update server values
        # Get server doc
        server_doc = database.db.servers.find_one({"server_id": message.guild.id})

        # Add member to member list if not in list
        server_members = server_doc.get("members", [])
        if message.author.id not in server_members:
            server_members.append(message.author.id)
            database.db.servers.update_one(
                {"server_id": message.guild.id},
                {"$set": {"members": server_members}},
            )

        server_data = user_doc["servers"].get(
            f"{message.guild.id}",
            {"messages": 0, "level": 0, "xp": 0, "last_message": None},
        )
        # logger.debug(server_data)

        server_data["messages"] += 1
        gained_server_xp = 100
        server_data["xp"] += gained_server_xp

        old_server_level = server_data["level"]
        new_server_level = math.floor(calc.level_for_experience(server_data["xp"], 200))
        # print(old_server_level, new_server_level)

        if old_server_level < new_server_level:
            server_data["level"] = new_server_level
            logger.info(
                f"[server] {message.author.name} has leveled up to level {new_server_level}"
            )
        # logger.debug(server_data)

        guild_id = f"{message.guild.id}"
        if guild_id in updated_doc["servers"]:
            updated_doc["servers"][guild_id].update(server_data)
        else:
            updated_doc["servers"][guild_id] = server_data
        # logger.debug(updated_doc)

        # Update docs
        database.db.users.update_one(
            {"user_id": message.author.id}, {"$set": updated_doc}
        )

    except Exception as e:
        # [05/05/24] It's late and I'm going insane fixing errors
        # [05/07/24] Im so glad this block exists
        logger.error(f"An error occured handling msg XP event: {e}")
        traceback.print_exc()
        raise e
