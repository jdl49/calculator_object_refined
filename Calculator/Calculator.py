from MathOperations import difference
from MathOperations.Addition import Addition
from MathOperations.difference import Difference

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
        return a * b

    def division(self, a, b):
        return a / b

    def squareroot(self, a):
        return a**(.5)

    def square(self, a):
        return a**2