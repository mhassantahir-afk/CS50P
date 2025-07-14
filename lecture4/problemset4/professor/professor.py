import random
import sys

# entered needed libraries
def main():
    # entered required variables
    levels = int(get_level())
    count = 10
    correct = 0
    a3 = 0
    while count>0:
        a1, a2 = generate_integer(levels)
        counter = 3
        while counter!=0:
            a3 = int(input(f"{a1} + {a2} = "))
            counter-=1
            if a3 == a1+a2:
                correct += 1
                break
            else:
                print("EEE")
            if counter == 0:
                print(f"{a1} + {a2} = {a1+a2}")
        count-=1
    print(f"Score: {correct}")
    sys.exit()


def get_level():
    while True:# to check consistently for correct input
        a = input("Level: ")
        if a == '1' or a == '2' or a == '3':
            return a


def generate_integer(level):
    a1 = 0
    a2 = 0
    match level:# to generate random int based on level
        case 1:
            a1 = random.randint(0,9)
            a2 = random.randint(0,9)
        case 2:
            a1 = random.randint(10,99)
            a2 = random.randint(10,99)
        case 3:
            a1 = random.randint(100,999)
            a2 = random.randint(100,999)
    return a1, a2

if __name__ == "__main__":
    main()
