import json
from pathlib import Path
from datetime import datetime

# Path to the history file
HISTORY_FILE = Path("data/history.json")


def log_conversation(data: dict) -> None:
    """
    Save a conversation to history.json.
    """

    data["timestamp"] = datetime.now().isoformat()

    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    else:
        history = []

    history.append(data)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def load_history() -> list:
    """
    Load all saved conversations.
    """

    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []