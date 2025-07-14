# taking input of the as answer for question
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.lower().strip(" ")

# now i use if else statements to compare and generate an output
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
