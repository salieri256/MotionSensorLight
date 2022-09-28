from machine import Pin
from PicoGpioNumber import PicoGpioNumber

class PicoLED:
    __PIN_NUMBER = PicoGpioNumber(25)
    
    def __init__(self):
        self.__pin = Pin(PicoLED.__PIN_NUMBER.value, Pin.OUT)
    
    def on(self):
        self.__pin.on()
    
    def off(self):
        self.__pin.off()
