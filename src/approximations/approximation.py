class Approximation:
    TRIPLE_POINT = 0.01

    def __init__(self, name):
        self.name = name

    def evaluate(self, temperature):
        """
        Method to calculate a saturated water vapor pressure under a measured temperature.

        :param temperature: Measured temperature in celsius degrees (°C).
        :return: Saturated water vapor pressure in pascals (Pa).
        """
        raise NotImplementedError
