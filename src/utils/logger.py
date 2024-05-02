import os
import inspect
from datetime import datetime
from rich import print
from rich.text import Text


class Logger:
    def __init__(self):
        self.colors = {
            "primary": "medium_purple2",
            "neutral": "grey46",
        }
        self.prefix = " >> "
        self.levels = {
            "debug": "blue",
            "info ": "green",
            "warn ": "yellow",
            "error": "red",
            "fatal": "bold red on white",
        }

    def get_caller_function_name(self):
        caller_frame = inspect.stack()[3]
        # print(inspect.stack())
        caller_path = os.path.relpath(
            inspect.getfile(caller_frame[0]), start=os.getcwd()
        )
        return f"[{caller_path}]"

    def log(self, level, message):
        timestamp = Text(f"[{datetime.now().isoformat()}]", style="gray")
        formatted_timestamp = (
            f"[{self.colors['neutral']}]{timestamp}[/{self.colors['neutral']}]"
        )
        formatted_level = f"[{self.levels[level]}]{level}[/{self.levels[level]}]"
        caller_info = self.get_caller_function_name()
        formatted_caller_info = (
            f"[{self.colors['neutral']}]\{caller_info}[/{self.colors['neutral']}]"
        )

        formatted_message = f"{formatted_timestamp} {formatted_level}{self.prefix}{formatted_caller_info} {message}"
        print(formatted_message)

    def debug(self, message):
        self.log("debug", message)

    def info(self, message):
        self.log("info ", message)

    def warn(self, message):
        self.log("warn ", message)

    def error(self, message):
        self.log("error", message)

    def fatal(self, message):
        self.log("fatal", message)


logger = Logger()

if __name__ == "__main__":
    logger.debug("Message")
    logger.info("Message")
    logger.warn("Message")
    logger.error("Message")
    logger.fatal("Message")
