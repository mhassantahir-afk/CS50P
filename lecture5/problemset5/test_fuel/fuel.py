def main():
    fuel = convert(input("Fraction: "))
    f = gauge(fuel)
    print(f)


def convert(fraction):
    while True:
# try checks for errors and reurns float for the value
        try:
            f1, f2 = fraction.split("/")
# if is to check if denominator is smaller then the nueminator
            if int(f1)/int(f2)> 1:
                continue
            return int((int(f1)/int(f2))*100)
        except(ValueError, ZeroDivisionError):
            if int(f2) == 0:
                raise ZeroDivisionError
            else:
                raise ValueError


def gauge(percentage):
    if percentage == 100 or percentage == 99:
        return "F"
    elif percentage == 0 or percentage == 1:
        return "E"
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
