import inflect # importing required libraray

p = inflect.engine() # definig p with the required function

my_list = [] # fdefinig list

while(True): # loop inputs list until ctrl D is hit
    try:
        my_list.append(input())
    except(EOFError):
        break

my_list = p.join(my_list) # joining list in required format

print("Adieu, adieu, to",my_list)
