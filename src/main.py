from approximations.hyland_wexler import HylandWexler
from approximations.iapws_if97 import IAPWS


def use_approximation(approximation, temperature):
    pressure = approximation.evaluate(temperature)
    print(f'{approximation.name} -> Pressure @ {temperature} °C: {pressure} KPa')


def main():
    use_approximation(HylandWexler(), 26.85)
    use_approximation(IAPWS(), 26.85)

    use_approximation(HylandWexler(), -15)
    use_approximation(IAPWS(), -15)


if __name__ == "__main__":
    main()
