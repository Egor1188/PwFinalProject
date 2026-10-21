import logging

from loguru import logger

from configs.config import Config


class PropagateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


class ConfigurateLogger:
    def __init__(self, config: Config):
        self.file_path = config.log.log_path
        self.colorize = True

        if config.log.remove_stderr:
            [logger.remove(stderr._id) for stderr in self.stderr_handlers]

        if not self.file_path_handler_available:
            # logger.remove(0)
            logger.add(
                self.file_path,
                colorize=config.log.colorize,
                level=config.log.level,
                format=config.log.format,
            )
            logger.info(f"Logging is set to file path - {self.file_path}")
        if not self.propagate_handler_available:
            logger.add(
                PropagateHandler(), level=config.log.level, colorize=config.log.colorize, format=config.log.format
            )
            logger.info("Success init propagate handler logging")

        logging.getLogger("sqlalchemy").setLevel(logging.ERROR)

    @property
    def handlers(self):
        return logger._core.handlers

    @property
    def file_path_handler_available(self):
        available_file_handlers = list(
            filter(lambda x: (getattr(x._sink, "_path", None) == self.file_path), self.handlers.values())
        )
        return True if len(available_file_handlers) > 0 else False

    @property
    def propagate_handler_available(self):
        propagate_handlers = list(
            filter(lambda x: (isinstance(getattr(x._sink, "_handler", None), PropagateHandler)), self.handlers.values())
        )
        return True if len(propagate_handlers) > 0 else False

    @property
    def stderr_handlers(self):
        stderr_handlers = list(filter(lambda x: (getattr(x, "_name", None) == "<stderr>"), self.handlers.values()))
        return stderr_handlers
