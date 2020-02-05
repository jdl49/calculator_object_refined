class Square:

    @staticmethod
    def square(base):
        if isinstance(base, list):
            return Square.squareList(base)
        return base**2
'''
    @staticmethod
    def squareList(valueList):
        result = 0
        for value in valueList:
            result = Square.square(result, value)

        return result
'''