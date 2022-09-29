from SG92RRotationDegree import SG92RRotationDegree

class SG92RPulseWidthPerMilliSecond:
    __MIN_VALUE = 0.5
    __MAX_VALUE = 2.4
    
    def __init__(self, value: float):
        if value < SG92RPulseWidthPerMilliSecond.__MIN_VALUE or SG92RPulseWidthPerMilliSecond.__MAX_VALUE < value:
            raise Exception('SG92R-pulse-width-per-second is incorrect.')
        
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @staticmethod
    def calc_duty_width(degree: SG92RRotationDegree):
        pulse_width_amplitude = SG92RPulseWidthPerMilliSecond.__MAX_VALUE - SG92RPulseWidthPerMilliSecond.__MIN_VALUE
        degree_amplitude = SG92RRotationDegree.MAX_VALUE - SG92RRotationDegree.MIN_VALUE
        pulse_width_per_degree = pulse_width_amplitude / degree_amplitude
        duty_width = pulse_width_per_degree * (degree.value - SG92RRotationDegree.MIN_VALUE) + SG92RPulseWidthPerMilliSecond.__MIN_VALUE
        return SG92RPulseWidthPerMilliSecond(duty_width)
        