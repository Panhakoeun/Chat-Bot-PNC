import importlib
import logging
import re
from typing import Any

from .config import BOT_USERNAME, TOKEN, configure_logging
from .responder import handle_response

logger = configure_logging()


async def start_command(update: Any, context: Any) -> None:
    await update.message.reply_text(
        "Hello! I am your PNC Telegram assistant.\n"
        "Ask me anything about Passerelles Numeriques Cambodia."
    )


async def help_command(update: Any, context: Any) -> None:
    await update.message.reply_text(
        "You can ask me questions about verified PNC information.\n\n"
        "Examples:\n"
        "- What is PNC?\n"
        "- What is the mission of PNC?\n"
        "- What programs does PNC offer?\n"
        "- How many students are at PNC?\n"
        "- Where is PNC located?\n"
        "- How many graduates does PNC have?\n"
        "- Is PNC recognized by the Ministry of Education?"
    )


async def custom_command(update: Any, context: Any) -> None:
    await update.message.reply_text("Ask me a question about PNC and I will do my best to help.")


async def handle_message(update: Any, context: Any) -> None:
    if not update.message or not update.message.text:
        return

    message_type = update.message.chat.type
    text = update.message.text.strip()
    logger.info('User (%s) in %s: "%s"', update.message.chat.id, message_type, text)

    if message_type in {"group", "supergroup"}:
        is_mentioned = BOT_USERNAME.lower() in text.lower()
        is_reply_to_bot = bool(
            update.message.reply_to_message
            and update.message.reply_to_message.from_user
            and update.message.reply_to_message.from_user.username
            and update.message.reply_to_message.from_user.username.lower() == BOT_USERNAME.lstrip("@").lower()
        )
        if not is_mentioned and not is_reply_to_bot:
            return

        cleaned_text = re.sub(re.escape(BOT_USERNAME), "", text, flags=re.IGNORECASE).strip()
        response = handle_response(cleaned_text)
    else:
        response = handle_response(text)

    logger.info("Bot: %s", response)
    await update.message.reply_text(response)


async def error_handler(update: object, context: Any) -> None:
    logger.exception("Update %s caused error: %s", update, context.error)


def run_bot() -> None:
    try:
        telegram_ext = importlib.import_module("telegram.ext")
    except ImportError as exc:
        raise ImportError(
            "python-telegram-bot is not installed. Install it with: pip install python-telegram-bot"
        ) from exc

    if TOKEN == "YOUR_BOT_TOKEN":
        raise ValueError("Please set TELEGRAM_BOT_TOKEN before running the bot.")

    application = telegram_ext.Application
    command_handler = telegram_ext.CommandHandler
    message_handler = telegram_ext.MessageHandler
    filters = telegram_ext.filters

    logger.info("Bot is starting...")
    app = application.builder().token(TOKEN).build()
    app.add_handler(command_handler("start", start_command))
    app.add_handler(command_handler("help", help_command))
    app.add_handler(command_handler("custom", custom_command))
    app.add_handler(message_handler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    logger.info("Polling...")
    app.run_polling(poll_interval=2)

