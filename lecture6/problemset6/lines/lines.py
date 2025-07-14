import sys

counter = 0

try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            name = sys.argv[1]
            with open(name, "r") as file:
                for line in file:
                    line = line.lstrip(" ")
                    if line.startswith("#") or line == "\n" or line.startswith("\'\'\'"):
                        continue
                    else:
                        counter += 1
            print(counter)
        else:
            print("Not a Python file")
            sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
except (FileNotFoundError):
    print("File does not exist")


