import unittest
import math_quiz_func as m

class TestMathQuizFunctions(unittest.TestCase):

    def test_addition_1_plus_1(self):
        # Does 1 + 1 work
        question, answer = m.addition(1, 1)
        self.assertEqual([question, answer], ['1 + 1', 2])
    
    def test_subtraction_2_minus_1(self):
        # Does 2 - 1 work
        question, answer = m.subtraction(2, 1)
        self.assertEqual([question, answer], ['2 - 1', 1])
    
    def test_multiplication_2_times_2(self):
        # Does 2 x 2 work
        question, answer = m.multiplication(2, 2)
        self.assertEqual([question, answer], ['2 * 2', 4])
        
    def test_division_4_divide_2(self):
        # Does 4 / 2 work
        question, answer = m.division(4, 2)
        self.assertEqual([question, answer], ['4 / 2', 2])

    def test_generate_question_two(self):
        # Does generate_question work with two numbers
        question, answer = m.generate_question([1, 1])
        self.assertIn(question, ['1 + 1', '1 - 1'])

    def test_generate_answer_two(self):
        # Does generate_question work with two numbers
        question, answer = m.generate_question([1, 1])
        self.assertIn(answer, [2, 0])

    def test_generate_question_four(self):
        # Does generate_question work with four numbers
        question, answer = m.generate_question([1, 1, 1, 1])
        self.assertIn(question, ['1 + 1', '1 - 1', '1 * 1', '1 / 1'])

    def test_generate_answer_four(self):
        # Does generate_question work with four numbers
        question, answer = m.generate_question([1, 1, 1, 1])
        self.assertIn(answer, [2, 0, 1, 1])

unittest.main()
