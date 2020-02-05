import unittest

from MathOperations.Addition import Addition
from MathOperations.difference import Difference
from MathOperations.divide import Divide
from MathOperations.multiply import Multiply
from MathOperations.square import Square
from MathOperations.squareroot import SquareRoot

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Difference.difference(1,2))

    def test_MathOperations_sum_list(self):
        valuelist = (1,2,3)
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_difference_list(self):
        valuelist = (1,2,3)
        self.assertEqual(-4, Difference.difference(valuelist))

    def test_MathOperations_multiply(self):
        self.assertEqual(2, Multiply.multiply(2,2))

    def test_MathOperations_multiply_list(self):
        valuelist = (1,2,3)
        self.assertEqual(6, Multiply.multiply(valuelist))

    def test_MathOperations_divide(self):
        self.assertEqual(2, Divide.divide(4,2))

    def test_MathOperations_squareRoot(self):
        self.assertEqual(2, SquareRoot.squareRoot(4))

    def test_MathOperations_square(self):
        self.assertEqual(4, Square.square(2))

    def test_MathOperations_divide_list(self):
        valuelist = (8,2,2)
        self.assertEqual(2, Divide.divide(valuelist))


