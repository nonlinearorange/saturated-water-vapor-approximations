import math

from approximations.approximation import Approximation


class IAPWS(Approximation):
    """
        IAPWS IF-97 approximation class for saturated water vapor pressure.

        This approximation is valid within the range of 0.0 °C and 373.946 °C.
        """

    def __init__(self):
        super().__init__("IAPWS IF-97")

    def evaluate(self, temperature):
        t = temperature + 273.15
        return self.evaluate_region_4(t) * 1000000.0

    @staticmethod
    def evaluate_region_4(t):
        n1 = 1167.0521452767
        n2 = -724213.16703206
        n3 = -17.073846940092
        n4 = 12020.82470247
        n5 = -3232555.0322333
        n6 = 14.91510861353
        n7 = -4823.2657361591
        n8 = 405113.40542057
        n9 = -0.23855557567849
        n10 = 650.17534844798

        th = t + n9 / (t - n10)
        a = (th + n1) * th + n2
        b = (n3 * th + n4) * th + n5
        c = (n6 * th + n7) * th + n8

        return math.pow(2.0 * c / (-b + math.sqrt(math.pow(b, 2) - 4.0 * a * c)), 4)
