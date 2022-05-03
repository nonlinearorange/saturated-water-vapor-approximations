from approximations.hyland_wexler import HylandWexler


def main():
    temperature = 25.0  # °C
    approximation = HylandWexler()
    pressure = approximation.evaluate(temperature)

    print(f'Pressure @ {temperature} °C: {pressure} Pa')


if __name__ == "__main__":
    main()
