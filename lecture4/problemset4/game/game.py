# importing needed libraries
import random
import sys
# for checking positive number
def check_positive(x):
    if x > 0:
        return 0
    else:
        return 1
# for guess check
def check_guess(a, g):
    if g>0:
        if g == a:
            print("Just right!")
            return 0
        elif g > a:
            print("Too large!")
        elif g< a:
            print("Too small!")

    return 1

def main():
    h = 1
    while(h):
        try:
            a = int(input("Upper Limit(1-A): "))
            h = check_positive(a)
        except(ValueError):
            continue

    r = random.randint(1, a)

    h= 1
    while(h):
        try:
            g = int(input("Guess: "))
            h = check_guess(r, g)
        except(ValueError):
            continue
    sys.exit()

main()
