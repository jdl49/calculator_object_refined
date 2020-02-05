class Divide:

    @staticmethod
    def divide(numarator, denominator=None):
        if isinstance(numarator, list):
            return Divide.divideList(numarator)
        return numarator / denominator

    @staticmethod
    def divideList(valueList):
        result = 0
        for value in valueList:
            if result == 0:
                result = value

            else:
                result = Divide.divide(result, value )

        return result