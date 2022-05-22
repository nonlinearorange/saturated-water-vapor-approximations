from matplotlib import pyplot as plt

from approximations.approximation import Approximation
from approximations.hyland_wexler import HylandWexler
from approximations.iapws_if97 import IAPWS
from approximations.its_90 import ITS90


def plot_approximations(approximations: list[Approximation]):
    temperatures = list(range(0, 50, 1))
    for approximation in approximations:
        plt.plot(temperatures, [approximation.evaluate(t) for t in temperatures], label=f"{approximation.name}")

    plt.ylabel("Pressure in Pa")
    plt.xlabel("Temperature in °C")
    plt.legend()
    plt.show()


def use_approximation(approximation: Approximation, temperature):
    pressure = approximation.evaluate(temperature)
    print(f'{approximation.name} -> Pressure @ {temperature} °C: {pressure} Pa')


def use_approximations(approximations: list[Approximation]):
    for item in approximations:
        use_approximation(item, 28.0)


def main():
    approximations = [HylandWexler(), IAPWS(), ITS90()]
    use_approximations(approximations)
    plot_approximations(approximations)


if __name__ == "__main__":
    main()
