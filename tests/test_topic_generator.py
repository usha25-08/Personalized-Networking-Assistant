import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services.topic_generator import generate_topics
def test_generate_topics_returns_list():

    result = generate_topics(
        ["Artificial Intelligence", "Sustainability"],
        ["Machine Learning"]
    )

    assert isinstance(result, list)
def test_generate_topics_returns_at_least_one_topic():

    result = generate_topics(
        ["Artificial Intelligence", "Sustainability"],
        ["Machine Learning"]
    )

    assert len(result) >= 1
def test_generate_topics_returns_strings():

    result = generate_topics(
        ["Artificial Intelligence", "Sustainability"],
        ["Machine Learning"]
    )

    for topic in result:
        assert isinstance(topic, str)
def test_generate_topics_returns_unique_topics():

    result = generate_topics(
        ["Artificial Intelligence", "Sustainability"],
        ["Machine Learning"]
    )

    assert len(result) == len(set(result))