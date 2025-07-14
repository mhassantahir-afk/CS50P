# exp variable means expression takes input as string
exp = input("Expression: ")

# extra caution if user mistakenly puts space ber=fore or after expression
exp = exp.strip(" ")

# to split against space and store values into x, y, z
x, y, z = exp.split(" ")

# turn x and z into float
x = float(x)
z = float(z)

# using match case statements for y
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
