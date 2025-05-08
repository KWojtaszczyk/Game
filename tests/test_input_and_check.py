import pytest
from unittest import mock
from input_and_check import get_answer_to_question, get_q_number, get_p_number, check_the_answer


def test_get_p_number_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    with mock.patch("builtins.print") as mock_print:
        assert get_p_number() == 3
        mock_print.assert_called_with("Opening the game for 3 players")


def test_get_p_number_too_many_players(monkeypatch):
    inputs = iter(["6", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch("builtins.print") as mock_print:
        assert get_p_number() == 3
        mock_print.assert_any_call("Too many players. Game only available up to 5 players. Choose again")
        mock_print.assert_any_call("Opening the game for 3 players")


def test_get_p_number_non_numeric(monkeypatch):
    inputs = iter(["abc", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch("builtins.print") as mock_print:
        assert get_p_number() == 2
        mock_print.assert_any_call("Incorrect input")


def test_get_q_number_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    assert get_q_number() == 10


def test_get_q_number_out_of_range(monkeypatch):
    inputs = iter(["20", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch("builtins.print") as mock_print:
        assert get_q_number() == 5
        mock_print.assert_any_call("Invalid input. Please enter a number between 1 and 15.")


def test_get_q_number_non_numeric(monkeypatch):
    inputs = iter(["xyz", "7"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch("builtins.print") as mock_print:
        assert get_q_number() == 7
        mock_print.assert_any_call("Invalid input.")


def test_get_answer_to_question_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "B")
    assert get_answer_to_question() == "B"


def test_get_answer_to_question_invalid_then_valid(monkeypatch):
    inputs = iter(["E", "A"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch("builtins.print") as mock_print:
        assert get_answer_to_question() == "A"
        mock_print.assert_any_call("Invalid answer.")


def test_check_the_answer_correct():
    assert check_the_answer("A", ["Question", "OptA", "OptB", "OptC", "OptD", "A"])


def test_check_the_answer_incorrect():
    assert not check_the_answer("B", ["Question", "OptA", "OptB", "OptC", "OptD", "A"])
