def main():
    dollars = (dollars_to_float(input("How much was the meal? ")))
    percent = (percent_to_float(input("What percentage would you like to tip? ")))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # first i remove the $ sign from the input string
    d = d.strip("$")

    # then i use return function to get a float as return
    return float(d)


def percent_to_float(p):
    # i used .strip function to remove % sign from the string
    p = p.strip("%")

    # turned it into a float
    p = float(p)

    # divided it by 100
    p = p/100

    # used return to get the value in float
    return float(p)


main()
