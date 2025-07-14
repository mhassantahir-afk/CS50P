# dictionary for menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Function defined for checking manu items

def menu_check():
    # variable sum
    sum = 0.00
    # while loop runs until ctrl d is hit
    while True:
        try:
            d = input("Item: ")
            d = d.title()
            # if statement checks if entry is in dictionary
            if d in menu:
                # Sum is added and total is calculated
                sum += menu[d]
                print("Total: $%.2f" %sum)
        except(EOFError):
            # if ctrl d is hit then program ends
            print("\n")
            break

menu_check()
