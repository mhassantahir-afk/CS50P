import sys
import csv

s = {}
r = []
x = {'first': '', 'last': '', 'house': ''}

try:
    if len(sys.argv) == 3:
        if(sys.argv[1].endswith(".csv")):
            file = sys.argv[1]
            newfile = sys.argv[2]
            with open(file, "r") as old:
                s = csv.DictReader(old)
                fieldnames = ['first','last','house']
                for i in s:
                    a,b = i['name'].split(', ')
                    x = {
                        'first' : b,
                        'last' : a,
                        'house' : i['house']
                        }
                    r.append(x)

            with open(newfile, "w") as new:
                writer = csv.DictWriter(new, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(r)


    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
except FileNotFoundError:
    print(f"could not read {sys.argv[1]}")
    sys.exit(1)

