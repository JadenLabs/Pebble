from src.base.config import config


def bool_to_string(bool_item: bool, true_str: str, false_str: str):
    return true_str if bool_item else false_str


def bool_to_status_emoji(bool_item: bool):
    return bool_to_string(
        bool_item=bool_item,
        true_str=config.emojis["green_check_box"],
        false_str=config.emojis["red_cross_box"],
    )
