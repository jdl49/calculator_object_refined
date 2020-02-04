import unittest

from MathOperations.Addition import Addition
from MathOperations.difference import Difference

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator

    def test_instantiate_calculator(self):
        calculator = Calculator()

        self.assertIsInstance(calculator, Calculator)

    def test_calculator_return_addition(self):
        calculator = Calculator()
        result = calculator.addition(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(4, 2)
        self.assertEqual(2, result)

    def test_calculator_access_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(4, 2)
        self.assertEqual(2, calculator.result)

    def test_calculator_access_addition(self):
        calculator = Calculator()
        result = calculator.subtraction(1, 2)
        self.assertEqual(-1, calculator.result)

    def test_multipe_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        calculator3 = Calculator()

        calculator3.addition(calculator1.addition(1,2), calculator2.subtraction(3,4))

        self.assertEqual(2, calculator3.result)
if __name__ == '__main__':
    unittest.main()
