import logging
import os
from typing import Final

TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
BOT_USERNAME: Final = os.getenv("TELEGRAM_BOT_USERNAME", "@infopnc_bot")


def configure_logging() -> logging.Logger:
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        level=logging.INFO,
    )
    return logging.getLogger(__name__)

