class SquareRoot:

    @staticmethod
    def squareRoot(radian):
        if isinstance(radian, list):
            return SquareRoot.squareRootList(radian)
        return radian**(.5)
'''
    @staticmethod
    def squareRootList(valueList):
        result = 0
        for value in valueList:
            result = SquareRoot.squareRoot(result, value)

        return result
'''