# defining fuction that will take fraction
def fuel_check(fuel):
    while True:
# try checks for errors and reurns float for the value
        try:
            fuel = input("Fraction: ")
            f1, f2 = fuel.split("/")
# if is to check if denominator is smaller then the nueminator
            if int(f1)/int(f2)> 1:
                continue
            return int(f1)/int(f2)
        except(ValueError, ZeroDivisionError):
            pass

fuel = 0
fuel = fuel_check(fuel)

# if else of checks if fuel is empty or full or something in between
if fuel == 1 or fuel == 0.99:
    print("F")
elif fuel == 0 or fuel == 0.01:
    print("E")
else:
    fuel *= 100
    print(f"{int(round(fuel))}%")
