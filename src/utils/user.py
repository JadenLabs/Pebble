import math
import random
from discord import Interaction, Message
from src.database.database import database
from src.base.config import config
from src.utils.logger import logger


def find_or_create(ctx: Interaction | Message) -> list[dict, bool]:
    try:
        user = ctx.user if ctx.user else ctx.author
    except AttributeError:
        user = ctx.author

    user_db = database.db.users
    user_doc = user_db.find_one({"user_id": user.id})
    logger.debug(f"Running doc check for {user.id}")
    user_is_new = False

    if not user_doc:
        user_is_new = True
        user_data = {
            "user_id": user.id,
            "username": user.name,
            "global_name": user.global_name,
            "total_messages": 0,
            "total_xp": 0,
            "servers": {},
        }
        # logger.debug(f"user_data: {user_data}")
        user_db.insert_one(user_data)
        user_doc = user_db.find_one({"user_id": user.id})
        logger.debug(f"Doc check for {user.id} failed, made new one")

    return user_doc, user_is_new


async def handle_msg_xp_event(message: Message):
    user_db = database.db.users
    user_doc = user_db.find_one({"user_id": message.author.id})

    # if message.channel.id == 1230356053590540300:
    #     await message.channel.send("got your message")

    updated_doc = {}
    updated_doc["total_messages"] = user_doc["total_messages"] + 1

    xp_range = (200, 400)
    gained_xp = random.randint(xp_range[0], xp_range[1])
    updated_doc["total_xp"] = user_doc["total_xp"] + gained_xp

    database.db.users.update_one({"user_id": message.author.id}, {"$set": updated_doc})
