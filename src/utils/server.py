import traceback
from discord import Guild
from src.database.database import database
from src.base.config import config
from src.utils.logger import logger


def find_or_create(guild: Guild):
    try:
        logger.debug(f"Running doc check for ${guild.id}")

        server_db = database.db.servers
        server_doc = server_db.find_one({"server_id": guild.id})

        if server_doc is not None:
            return server_doc

        server_data = {
            "server_id": guild.id,
            "name": guild.name,
            "grace": {"strictness": 1.25, "cooldown": 60},
            "leveling": {"multiplier": 200},
            "update_settings": {
                "channel": 1,
                "message": "Congrats on leveling up {user}! You are now level {level} �",
            },
            "members": [],
        }

        server_doc_result = server_db.insert_one(server_data)
        logger.debug(f"Server doc created for {guild.id}")

        server_doc = server_db.find_one({"server_id": guild.id})
        return server_doc
    except Exception as e:
        logger.error(f"An error occured with server.find_or_create {e}")
        traceback.print_exc()
        raise e