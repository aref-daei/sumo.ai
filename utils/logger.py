import logging
from datetime import datetime

from config import BASE_DIR


class Logger:
    """Logging system"""

    _instances = {}

    def __new__(cls, name: str = "SUMO.AI"):
        if name not in cls._instances:
            cls._instances[name] = super().__new__(cls)
        return cls._instances[name]

    def __init__(self, name: str = "SUMO.AI"):
        if hasattr(self, '_initialized') and self._initialized:
            return

        self.logger = logging.getLogger(name)

        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # Log directory
            log_dir = BASE_DIR / "logs"
            log_dir.mkdir(exist_ok=True)

            # Log file with date
            log_file = log_dir / f"app_{datetime.now().strftime('%Y%m%d')}.log"

            # Format
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            # File Handler
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

            # Prevent propagation to root logger to avoid duplicate messages
            self.logger.propagate = False

        self._initialized = True

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def debug(self, message: str):
        self.logger.debug(message)
