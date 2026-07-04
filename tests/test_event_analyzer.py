import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services.event_analyzer import analyze_event, DEFAULT_LABELS


def test_analyze_event_returns_list():
    result = analyze_event("AI for Sustainable Cities")
    assert isinstance(result, list)
def test_analyze_event_returns_max_three_themes():

    result = analyze_event("AI for Sustainable Cities")

    assert len(result) <= 3
def test_analyze_event_returns_at_least_one_theme():

    result = analyze_event("AI for Sustainable Cities")

    assert len(result) >= 1
def test_analyze_event_returns_strings():

    result = analyze_event("AI for Sustainable Cities")

    for theme in result:
        assert isinstance(theme, str)
from app.services.event_analyzer import DEFAULT_LABELS


def test_analyze_event_returns_valid_labels():

    result = analyze_event("AI for Sustainable Cities")

    for theme in result:
        assert theme in DEFAULT_LABELS