from tabulate import tabulate
import sys
import csv

try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            name = sys.argv[1]
            with open(name, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)
                data = {header: [] for header in headers}
                for row in reader:
                    for header, value in zip(headers, row):
                        data[header].append(value)

                print(tabulate(data, headers, tablefmt="grid"))
        else:
            print("Not a CSV file")
            sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
except (FileNotFoundError):
    print("File does not exist")
    sys.exit(1)


