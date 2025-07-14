#file = open("name.txt", "a")

#while True:
#    try:
#        file.write(f"{input("enter a name: ")}\n")
#    except EOFError:
#        break

#file.close()

with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line)

