from machine import Pin

class MotionSensor:
    def __init__(self, pin_number: PicoGpioNumber):
        self.__pin = Pin(pin_number.value, Pin.IN)
        self.__listeners = []
        self.__pin.irq(trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = self.__notify_listeners)
        
    def is_detecting_motion(self) -> bool:
        return True if self.__pin.value() is 1 else False
    
    def add_listener(self, listener):
        self.__listeners.append(listener)
        
    def remove_listener(self, listener):
        self.__listeners.remove(listener)
    
    def __notify_listeners(self, pin):
        for listener in self.__listeners:
            listener()