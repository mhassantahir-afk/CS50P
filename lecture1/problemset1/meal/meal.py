def main():
# using function to add time float value to variable sum
    sum = convert(input("Enter Time: "))
    sum = sum * 3600


# if else if statements to check for time
    if sum >= 25200 and sum <= 28800:
        print("breakfast time")
    elif sum >= 43200 and sum <= 46800:
        print("lunch time")
    elif sum >= 64800 and sum <= 68400:
        print ("dinner time")


def convert(time):

# using variable time to store value of time in float
    time = time.strip(" ")
    x, y = time.split(":")
    y = float(y)/60
    x = float(x)
    time = float(x + y)
    return time



if __name__ == "__main__":
    main()
