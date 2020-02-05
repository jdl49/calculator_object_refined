
import unittest

from Calculator.Calculator import Calculator

from MathOperations.Addition import Addition
from MathOperations.difference import Difference
from MathOperations.divide import Divide
from MathOperations.multiply import Multiply


class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_addition(self):
        result = self.calculator.addition(1, 2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self):
        result = self.calculator.subtraction(4, 2)
        self.assertEqual(2, result)

    def test_calculator_multiplication(self):
        result = self.calculator.multiplication(2, 2)
        self.assertEqual(4, result)

    def test_calculator_division(self):
        result = self.calculator.division(3, 1)
        self.assertEqual(3, result)

    def test_calculator_squareroot(self):
        result = self.calculator.squareroot(4)
        self.assertEqual(2, result)

    def test_calculator_square(self):
        result = self.calculator.square(2)
        self.assertEqual(4, result)

    def test_calculator_access_Addition_result(self):
        self.calculator.addition(1, 2)
        self.assertEqual(3, self.calculator.result)

    def test_calculator_access_subtraction_result(self):
        self.calculator.subtraction(1, 2)
        self.assertEqual(-1, self.calculator.result)

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_difference_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(-4, Difference.difference(valuelist))

    def test_calculator_access_multiply_result(self):
        self.calculator.multiplication(2, 2)
        self.assertEqual(4, self.calculator.result)

    def test_MathOperations_multiply_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Multiply.multiply(valuelist))

    def test_calculator_access_divide_result(self):
        self.calculator.division(4, 2)
        self.assertEqual(2, self.calculator.result)

    def test_calculator_access_squareRoot_result(self):
        self.calculator.squareroot(4)
        self.assertEqual(2, self.calculator.result)

    def test_calculator_access_square_result(self):
        self.calculator.square(2)
        self.assertEqual(4, self.calculator.result)

    def test_MathOperations_divide_list(self):
        valuelist = [8, 2, 2]
        self.assertEqual(2, Divide.divide(valuelist))

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.addition(calculator1.addition(1, 2), calculator2.subtraction(3, 4))
        self.assertEqual(2, self.calculator.result)


if __name__ == '__main__':
    unittest.main()
