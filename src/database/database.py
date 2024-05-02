from pymongo import MongoClient
from pymongo.server_api import ServerApi
from src.base.config import config
from src.utils.logger import logger


class Database:
    def __init__(self, mongo_uri: str) -> None:
        logger.debug("Attempting database connection")
        try:
            self.client = MongoClient(
                mongo_uri,
                server_api=ServerApi("1"),
            )
            self.db = self.client["production"]
            logger.debug("Database connection successful")
        except Exception as err:
            logger.error(f"An error occured when connecting to the database: {err}")
            raise err

        self.guilds = self.db.guilds


database = Database(config.mongo_uri)
