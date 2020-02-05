class Multiply:

    @staticmethod
    def multiply(multiplier, multiplicand=None):
        if isinstance(multiplier, list):
            return Multiply.multiplyList(multiplier)
        return multiplier * multiplicand

    @staticmethod
    def multiplyList(valueList):
        result = 1
        for value in valueList:
            result = Multiply.multiply(result, value)

        return result

