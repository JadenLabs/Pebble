from discord import Embed
from src.base.config import config

no_user_perms_embed = Embed(
    color=config.colors["error"],
    description=f"You do not have the needed permissions to run this command.",
)
