import math

from approximations.approximation import Approximation


class ITS90(Approximation):
    """
    ITS-90 approximation class for saturated water vapor pressure.

    This approximation is valid within the range of -100.0 °C and 100.0 °C.
    """

    def __init__(self):
        super().__init__("ITS-90")

    def evaluate(self, temperature):
        t = temperature + 273.15

        if t < self.TRIPLE_POINT:
            return self.evaluate_ice(t)
        else:
            return self.evaluate_water(t)

    @staticmethod
    def evaluate_ice(t):
        k0 = -5.8666426E3
        k1 = 2.232870244E1
        k2 = 1.39387003E-2
        k3 = -3.4262402E-5
        k4 = 2.7040955E-8
        k5 = 6.7063522E-1

        return math.exp(1 / t * k0 + k1 * t + k2 * math.pow(t, 2) + k3 * math.pow(t, 3) + k4 * math.pow(t, 4) +
                        k5 * math.pow(t, 5))

    @staticmethod
    def evaluate_water(t):
        g0 = -2.8365744E3
        g1 = -6.028076559E3
        g2 = 1.954263612E1
        g3 = -2.737830188E-2
        g4 = 1.6261698E-5
        g5 = 7.0229056E-10
        g6 = -1.8680009E-13
        g7 = 2.7150305

        return math.exp(1 / math.pow(t, 2) * g0 + 1 / t * g1 + g2 + g3 * t + g4 * math.pow(t, 2) +
                        g5 * math.pow(t, 3) + g6 * math.pow(t, 4) + g7 * math.log(t))
