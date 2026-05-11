import logging
import os
from pathlib import Path
from typing import Final
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
BOT_USERNAME: Final = os.getenv("TELEGRAM_BOT_USERNAME", "@infopnc_bot")


def configure_logging() -> logging.Logger:
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        level=logging.INFO,
    )
    return logging.getLogger(__name__)

