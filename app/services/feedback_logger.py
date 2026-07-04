import json
from pathlib import Path
from datetime import datetime

# Path to the feedback file
FEEDBACK_FILE = Path("data/feedback.json")


def log_feedback(suggestion: str, action: str) -> None:
    """
    Save user feedback (like/dislike) to feedback.json.
    """

    feedback = {
        "suggestion": suggestion,
        "action": action,
        "timestamp": datetime.now().isoformat()
    }

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            feedback_list = json.load(file)
    else:
        feedback_list = []

    feedback_list.append(feedback)

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
        json.dump(feedback_list, file, indent=4)


def load_feedback() -> list:
    """
    Load all saved feedback.
    """

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []