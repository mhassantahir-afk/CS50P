greet = input("Greeting: ")

greet = greet.lower().strip(" ")

for_hello = greet.startswith("hello")
for_h = greet.startswith("h")

if for_hello == True:
    print("$0")
elif for_h == True:
    print("$20")
else:
    print("$100")
