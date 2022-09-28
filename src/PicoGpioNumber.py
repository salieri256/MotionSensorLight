class PicoGpioNumber:
    __MIN_VALUE = 0
    __MAX_VALUE = 28
    
    def __init__(self, value: int):
        if value < PicoGpioNumber.__MIN_VALUE or PicoGpioNumber.__MAX_VALUE < value:
            raise Exception('Pico-GPIO-number is incorrect.')
        
        self.__value = value
    
    @property
    def value(self):
        return self.__value
