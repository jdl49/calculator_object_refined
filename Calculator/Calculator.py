from MathOperations import difference
from MathOperations.Addition import Addition
from MathOperations.difference import Difference
from MathOperations.divide import Divide
from MathOperations.multiply import Multiply
from MathOperations.square import Square
from MathOperations.squareroot import SquareRoot

class Calculator:

    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = Addition.sum(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = Difference.difference(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = Multiply.multiply(a, b)
        return self.result

    def division(self, a, b):
        self.result = Divide.divide(a, b)
        return self.result

    def squareroot(self, a):
        self.result = SquareRoot.squareRoot(a)
        return self.result

    def square(self, a):
        self.result = Square.square(a)
        return self.result