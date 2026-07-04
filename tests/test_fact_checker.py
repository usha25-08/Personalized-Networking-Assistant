import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services.fact_checker import fact_check
def test_fact_check_returns_string():

    result = fact_check("Artificial Intelligence")

    assert isinstance(result, str)
def test_fact_check_returns_non_empty_string():

    result = fact_check("Artificial Intelligence")

    assert len(result.strip()) > 0
def test_fact_check_invalid_topic():

    result = fact_check("asdfghjklqwerty123456")

    assert isinstance(result, str)
    assert len(result.strip()) > 0