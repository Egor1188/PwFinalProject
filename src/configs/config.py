import logging
import os
import random
import string
from pathlib import Path

import yaml


class BaseConfig:
    def __init__(
        self,
        config_data: dict | None = None,
        config_path: str | None = None,
    ):
        """
        :param config_data: use existing config data
        :param config_path: read config data from providable path if config_data = None
        """
        if config_data:
            self.config_data = config_data
        else:
            config_path = config_path or os.path.join(
                Path(__file__).parent.parent.parent, "configs", "config.yml"
            )
            with open(config_path) as data_file:
                self.config_data = yaml.full_load(data_file)


class Config(BaseConfig):
    def __init__(
        self,
        config_data: dict | None = None,
        config_path: str | None = None,
    ):
        super().__init__(config_data, config_path)
        self.log = Logger(self.config_data["Application"]["general"]["log"])


class Logger:
    def __init__(self, config_data: dict):
        self.level = config_data.get("level", logging.INFO)
        self.format = config_data.get(
            "format", "<green>{time}</green> {level} | {message}"
        )
        self.colorize = config_data.get("colorize", True)
        self.remove_stderr = config_data.get("remove_stderr", False)
        self.log_path = config_data.get(
            "path",
            os.path.join(
                Path(__file__).parent.parent.parent,
                "var",
                "logs",
                f"run_tests_log_{''.join(random.choices(string.digits, k=6))}.log",
            ),
        )
