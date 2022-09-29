from machine import PWM, Pin
from PicoGpioNumber import PicoGpioNumber
from SG92RRotationDegree import SG92RRotationDegree
from SG92RPulseWidthPerMilliSecond import SG92RPulseWidthPerMilliSecond

class SG92R:
    __FREQUENCY = 50
    
    def __init__(self, pwm_pin_number: PicoGpioNumber):
        self.__pwm_pin = PWM(Pin(pwm_pin_number.value))
        self.__pwm_pin.freq(SG92R.__FREQUENCY)
    
    def rotate(self, degree: SG92RRotationDegree):
        duty_width_per_s = SG92RPulseWidthPerMilliSecond.calc_duty_width(degree)
        duty_cycle_per_ns = duty_width_per_s.value * 1_000_000
        self.__pwm_pin.duty_ns( int(duty_cycle_per_ns) )
