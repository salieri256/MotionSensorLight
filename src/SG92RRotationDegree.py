class SG92RRotationDegree:
    MIN_VALUE = -90
    MAX_VALUE = 90
    
    def __init__(self, value: int):
        if value < SG92RRotationDegree.MIN_VALUE or SG92RRotationDegree.MAX_VALUE < value:
            raise Exception('SG92R-rotation-degree is incorrect.')
    
        self.__value = value
    
    @property
    def value(self):
        return self.__value
        