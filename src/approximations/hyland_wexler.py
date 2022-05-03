import math

from approximations.approximation import Approximation


class HylandWexler(Approximation):
    """
    Hyland-Wexler approximation class for saturated water vapor pressure.

    This approximation is valid within the range of -100 °C and 200 °C.
    """

    def evaluate(self, temperature):
        t = temperature + 273.15

        if t < self.TRIPLE_POINT:
            return self.evaluate_ice(t)
        else:
            return self.evaluate_water(t)

    @staticmethod
    def evaluate_ice(t):
        c1 = -5.6745359E3
        c2 = 6.3925247
        c3 = -9.6778430E-3
        c4 = 6.2215701E-7
        c5 = 2.0747825E-9
        c6 = -9.4840240E-13
        c7 = 4.1635019

        return math.exp(
            c1 / t + c2 + c3 * t + c4 * math.pow(t, 2) + c5 * math.pow(t, 3) + c6 * math.pow(t, 4) + c7 * math.log(t))

    @staticmethod
    def evaluate_water(t):
        c8 = -5.8002206E3
        c9 = 1.3914993
        c10 = -4.8640239E-2
        c11 = 4.1764768E-5
        c12 = -1.445209E-8
        c13 = 6.5459673

        return math.exp(c8 / t + c9 + c10 * t + c11 * math.pow(t, 2) + c12 * math.pow(t, 3) + c13 * math.log(t))
