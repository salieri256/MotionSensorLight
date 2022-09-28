import time
from PicoLED import PicoLED
from MotionSensor import MotionSensor
from SG92R import SG92R
from SG92RRotationDegree import SG92RRotationDegree
from PicoGpioNumber import PicoGpioNumber

class Main:
    def __init__(self):
        self.__led = PicoLED()
        self.__servo_1 = SG92R(PicoGpioNumber(0))
        self.__servo_2 = SG92R(PicoGpioNumber(1))
        self.__motion_sensor_1 = MotionSensor(PicoGpioNumber(2))
        self.__motion_sensor_2 = MotionSensor(PicoGpioNumber(3))
        
        self.__motion_sensor_1.add_listener(self.__on_change_sensor_value)
    
    def __on_change_sensor_value(self):
        if self.__motion_sensor_1.is_detecting_motion():
            self.__on_detect()
        else:
            self.__on_lose()
    
    def __on_detect(self):
        degree_for_turn_on = SG92RRotationDegree(-22)
        self.__led.on()
        self.__servo_1.rotate(degree_for_turn_on)
        self.__servo_2.rotate(degree_for_turn_on)
        
        time.sleep(0.2)
        
        self.__reset()
    
    def __on_lose(self):
        degree_for_turn_off = SG92RRotationDegree(22)
        self.__led.on()
        self.__servo_1.rotate(degree_for_turn_off)
        self.__servo_2.rotate(degree_for_turn_off)
        
        time.sleep(0.2)
        
        self.__reset()
        
    def __reset(self):
        degree_for_turn_neutral = SG92RRotationDegree(0)
        self.__led.off()
        self.__servo_1.rotate(degree_for_turn_neutral)
        self.__servo_2.rotate(degree_for_turn_neutral)

main = Main()