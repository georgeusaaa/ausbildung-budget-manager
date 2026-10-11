import pytest

from main import evaluate_budget, parse_amount


def test_parse_amount_accepts_comma_and_empty():
    assert parse_amount("250,50") == 250.5
    assert parse_amount("  ") == 0
    with pytest.raises(ValueError):
        parse_amount("abc")


def test_statuses():
    assert evaluate_budget(1100, [250, 450, 50, 200]) == ("ok", 150)
    assert evaluate_budget(1100, [250, 450, 50, 250]) == ("danger", 100)
    assert evaluate_budget(1100, [500, 500, 200, 0]) == ("over", 100)


def test_invalid_values():
    with pytest.raises(ValueError, match="Лимит"):
        evaluate_budget(0, [10])
    with pytest.raises(ValueError, match="отрицательными"):
        evaluate_budget(1000, [-5])
