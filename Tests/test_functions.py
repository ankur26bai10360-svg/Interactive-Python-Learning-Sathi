"""Tests for the Interactive Python Learning Companion.I used Python's built-in unittest module.
Since the program uses input() and print(), I used unittest.mock.patch
to give fake inputs, and redirect_stdout to capture what gets printed."""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

# so the tests can find main.py, Data/, Modules/ etc. in the main folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import main
from Data.Quiz import Quiz_sem1, ask_question


#helper data and functions

# a small fake question to test ask_question()
SAMPLE_QUESTION = {
    "unit": "Unit 1 - Test",
    "question": "What is 1 + 1?",
    "options": ["1", "2", "3", "4"],
    "answer": 1,}

# correct option numbers (1 to 4) for the 21 quiz questions,
# in the same order as they are written in Quiz.py
ALL_CORRECT = [1,2, 1,3,3, 2,3, 2,3, 1,2,1, 3, 3, 1, 1,1,4,3,4, 2]

# a wrong option for every question (never the same as the correct one)
ALL_WRONG = [(a % 4) + 1 for a in ALL_CORRECT]


def ask(user_inputs):
    """Runs ask_question() with fake inputs, returns (result, printed text)."""
    buffer = io.StringIO()
    with patch("builtins.input", side_effect=user_inputs), redirect_stdout(buffer):
        result = ask_question(SAMPLE_QUESTION, 1)
    return result, buffer.getvalue()


def run_quiz(answers):
    """Runs the whole quiz with fake answers and returns the printed output."""
    # first input = 'Press Enter to start', last input = 'Press Enter to return'
    inputs = [""] + [str(a) for a in answers] + [""]
    buffer = io.StringIO()
    with patch("builtins.input", side_effect=inputs), \
         patch("random.shuffle"), \
         patch("Data.Quiz.clear_screen"), \
         redirect_stdout(buffer):
        Quiz_sem1()
    return buffer.getvalue()


def run_main(choices):
    """Runs the main menu with fake choices and returns the printed output."""
    buffer = io.StringIO()
    with patch("builtins.input", side_effect=choices), \
         patch("main.clear_screen"), \
         redirect_stdout(buffer):
        main.main()
    return buffer.getvalue()


#test ask question

class TestAskQuestion(unittest.TestCase):

    def test_valid_answer_returns_index(self):
        # user types 2, function should return index 1
        result, _ = ask(["2"])
        self.assertEqual(result, 1)

    def test_first_option(self):
        result, _ = ask(["1"])
        self.assertEqual(result, 0)

    def test_last_option(self):
        result, _ = ask(["4"])
        self.assertEqual(result, 3)

    def test_letters_are_rejected(self):
        # "abc" is wrong, then "3" is right
        result, output = ask(["abc", "3"])
        self.assertEqual(result, 2)
        self.assertIn("Please enter a valid number.", output)

    def test_empty_input_is_rejected(self):
        result, output = ask(["", "1"])
        self.assertEqual(result, 0)
        self.assertIn("Please enter a valid number.", output)

    def test_decimal_is_rejected(self):
        result, output = ask(["2.5", "2"])
        self.assertEqual(result, 1)
        self.assertIn("Please enter a valid number.", output)

    def test_number_too_big(self):
        result, output = ask(["5", "1"])
        self.assertEqual(result, 0)
        self.assertIn("between 1 and 4", output)

    def test_zero_is_rejected(self):
        result, output = ask(["0", "4"])
        self.assertEqual(result, 3)
        self.assertIn("between 1 and 4", output)

    def test_negative_number_is_rejected(self):
        result, output = ask(["-1", "2"])
        self.assertEqual(result, 1)
        self.assertIn("between 1 and 4", output)

    def test_question_and_options_are_displayed(self):
        _, output = ask(["1"])
        self.assertIn("What is 1 + 1?", output)
        self.assertIn("1. 1", output)
        self.assertIn("4. 4", output)


#Test quiz

class TestQuizScoring(unittest.TestCase):

    def test_all_correct_gives_full_score(self):
        output = run_quiz(ALL_CORRECT)
        self.assertIn("Correct answers : 21", output)
        self.assertIn("Wrong answers   : 0", output)
        self.assertIn("Performance :OUTSTANDING", output)
        self.assertIn("Perfect score!", output)

    def test_all_wrong_gives_zero_score(self):
        output = run_quiz(ALL_WRONG)
        self.assertIn("Correct answers : 0", output)
        self.assertIn("Performance : better luck next time", output)
        self.assertIn("ANSWER REVIEW", output)

    def test_good_performance(self):
        # 13 right and 8 wrong = about 62%
        answers = ALL_CORRECT[:13] + ALL_WRONG[13:]
        output = run_quiz(answers)
        self.assertIn("Correct answers : 13", output)
        self.assertIn("Performance: V Good", output)

    def test_needs_improvement_performance(self):
        # 10 right and 11 wrong 47%
        answers = ALL_CORRECT[:10] + ALL_WRONG[10:]
        output = run_quiz(answers)
        self.assertIn("Correct answers : 10", output)
        self.assertIn("Performance   : Work hard", output)

    def test_total_questions_is_21(self):
        output = run_quiz(ALL_CORRECT)
        self.assertIn("Total questions : 21", output)

    def test_wrong_answer_review_shows_correct_answer(self):
        # we will get only the first question wrong (correct is option 1, so choose 2)
        answers = [2] + ALL_CORRECT[1:]
        output = run_quiz(answers)
        self.assertIn("Correct answers : 20", output)
        self.assertIn("Top-Down Design", output)
        self.assertIn("Breaking a large  problem into smaller problems", output)

    def test_invalid_input_during_quiz_does_not_crash(self):
        # we will put a wrong input ("abc") 
        inputs = [""] + ["abc"] + [str(a) for a in ALL_CORRECT] + [""]
        buffer = io.StringIO()
        with patch("builtins.input", side_effect=inputs), \
             patch("random.shuffle"), \
             patch("Data.Quiz.clear_screen"), \
             redirect_stdout(buffer):
            Quiz_sem1()
        self.assertIn("Correct answers : 21", buffer.getvalue())

    def test_intro_message_matches_real_question_count(self):
        # the start message says "N questions will be asked"
        # this should be the same as "Total Questions"
        output = run_quiz(ALL_CORRECT)
        self.assertIn("21 questions will be asked", output)


#Test main menu

class TestMainMenu(unittest.TestCase):

    def test_exit_option(self):
        output = run_main(["7"])
        self.assertIn("Thank you for using the Python Learning Companion", output)

    def test_menu_shows_all_options(self):
        output = run_main(["7"])
        self.assertIn("Unit 1", output)
        self.assertIn("Unit 5", output)
        self.assertIn("Quiz & Scores", output)
        self.assertIn("Exit Application", output)

    def test_each_unit_opens_correct_menu(self):
        units = {
            "1": "main.unit_1_menu",
            "2": "main.unit_2_menu",
            "3": "main.unit_3_menu",
            "4": "main.unit_4_menu",
            "5": "main.unit_5_menu",
        }
        for choice, function_name in units.items():
            with self.subTest(unit=choice):
                with patch(function_name) as fake_unit:
                    run_main([choice, "7"])
                    fake_unit.assert_called_once()

    def test_quiz_option_starts_quiz(self):
        with patch("main.Quiz_sem1") as fake_quiz:
            run_main(["6", "7"])
            fake_quiz.assert_called_once()

    def test_invalid_choice_shows_error(self):
        # 9 is invalid,press enter
        output = run_main(["9", "", "7"])
        self.assertIn("Invalid choice", output)

    def test_letter_choice_shows_error(self):
        output = run_main(["abc", "", "7"])
        self.assertIn("Invalid choice", output)

    def test_menu_returns_after_unit(self):
        # open unit 1, come back, then exit
        with patch("main.unit_1_menu"):
            output = run_main(["1", "7"])
        self.assertIn("Thank you", output)


if __name__ == "__main__":
    unittest.main()