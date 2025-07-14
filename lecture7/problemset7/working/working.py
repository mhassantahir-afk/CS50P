import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"([0-1]?[0-9]):?([0-5]?[0-9]?)\s(AM|PM)\s(to)\s([0-1]?[0-9]):?([0-5]?[0-9]?)?\s(AM|PM)", s):
        a = int(f"{match.group(1)}")
        b = int(f"{match.group(5)}")
        if a <= 12 and b <= 12:
            if match.group(3) == "PM" and a != 12:
                a += 12
            if match.group(7) == "PM" and b != 12:
                b += 12
            if match.group(3) == "AM" and a == 12:
                a = 0
            if match.group(7) == "AM" and b == 12:
                b = 0
            if match.group(2) != "" and match.group(6) != "":
                return(f"{a:02}:{match.group(2)} to {b:02}:{match.group(6)}")
            else:
                return(f"{a:02}:00 to {b:02}:00")
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
