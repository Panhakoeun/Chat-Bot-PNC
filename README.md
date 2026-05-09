# PNC Telegram Bot

This project is a Telegram chatbot for answering questions about Passerelles Numeriques Cambodia (PNC).

## Project Structure

- `main.py` - small entrypoint to start the bot
- `pnc_bot/config.py` - environment variables and logging
- `pnc_bot/models.py` - shared data models
- `pnc_bot/knowledge.py` - verified PNC knowledge base and matching hints
- `pnc_bot/responder.py` - question normalization and response logic
- `pnc_bot/telegram_bot.py` - Telegram handlers and polling startup
- `requirements.txt` - Python dependency list

## Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Set environment variables:

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_BOT_USERNAME="@your_bot_username"
```

Run the bot:

```powershell
python main.py
```
