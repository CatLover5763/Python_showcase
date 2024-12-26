def main():
    fraction = input("Fraction: ")
    result = convert(fraction)
    print(gauge(result))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            if y == 0:
                raise ZeroDivisionError
            elif int(x) > int(y) or x.isalpha() or y.isalpha():
                raise ValueError
            result = (int(x) / int(y))
            return round(result*100)
        except (ZeroDivisionError, ValueError):
            pass


def gauge(percentage):
    if 1 >= int(percentage):
        return "E"
    elif int(percentage) >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
