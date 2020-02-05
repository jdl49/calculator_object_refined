class Difference:

    @staticmethod
    def difference(minuend, subtraend=None):
        if isinstance(minuend, list):
            return Difference.defferenceList(minuend)
        return minuend - subtraend

    @staticmethod
    def defferenceList(valueList):
        result = 0
        for value in valueList:
            if result == 0:
                result = value
            else:
                result = Difference.difference(result, value)

        return result