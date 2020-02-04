import unittest

from MathOperations.Addition import Addition
from MathOperations.difference import Difference

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Difference.difference(1,2))

    def test_MathOperations_sum_list(self):
        valuelist = (1,2,3)
        self.assertEqual(6, Addition.sum(valuelist))