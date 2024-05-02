import os
import yaml
from types import SimpleNamespace
from dotenv import load_dotenv


class Config:
    def __init__(self, yaml_path: str, env_path: str = ".env"):
        # .env Loading
        load_dotenv(dotenv_path=env_path)
        self.token = os.getenv("token")
        self.client_id = os.getenv("client_id")
        self.mongo_uri = os.getenv("mongo_uri")

        # Yaml Loading
        self.config_dict = self.load_config(yaml_path)
        self.namespace = SimpleNamespace(**self.config_dict)
        vars(self).update(vars(self.namespace))

    def load_config(self, yaml_path) -> dict:
        with open(yaml_path, "r", encoding="UTF-8") as file:
            data = yaml.safe_load(file)
        return data


config = Config("./config.yaml", ".env")
