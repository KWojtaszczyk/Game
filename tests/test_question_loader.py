import csv
import pytest
from unittest import mock
from question_loader import load_questions, save_results, ask_question


sample_questions = [
    ["How many legs does a spider have?", "8", "6", "4", "10", "A"],
    ["Which planet is closest to the Sun?", "Mercury", "Venus", "Earth", "Mars", "A"]
]


def test_load_questions(tmp_path):
    question_file = tmp_path / "questions.csv"
    with open(question_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_questions)

    loaded_questions = load_questions(str(question_file))
    assert loaded_questions == sample_questions


def test_save_results(tmp_path):
    result_file = tmp_path / "results.txt"
    user_profile = "User123, Score: 80%"

    save_results(str(result_file), user_profile)

    with open(result_file, 'r', encoding='utf-8') as f:
        contents = f.read().strip()

    assert user_profile in contents


def test_ask_question():
    row = ["How many legs does a spider have?", "8", "6", "4", "10", "A"]

    expected_output = [
        "Question: How many legs does a spider have?",
        "A) 8",
        "B) 6",
        "C) 4",
        "D) 10"
    ]

    with mock.patch("builtins.print") as mock_print:
        ask_question(row)

        mock_print.assert_has_calls([mock.call(line) for line in expected_output])

        assert mock_print.call_count == 5

