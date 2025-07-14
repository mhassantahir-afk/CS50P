import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"src=\"(https?)(://)(?:www\.)?(youtube)\.com/embed(/\w+)\"", s):
        a,b = match.group(3).split("b")
        c = match.group(1)
        if match.group(1) == "http":
            c = f"{match.group(1)}s"

        i = 1
        while True:
            if i == 1:
                print(c, end="")
            elif match.group(i) != "None" and i != 3:
                print(match.group(i), end="")
            elif i == 3:
                print(f"{a}.b{b}", end="")
            i+=1
            if i == 5:
                print()
                break
        sys.exit(0)



if __name__ == "__main__":
    main()
