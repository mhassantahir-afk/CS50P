def main():
    greet = input("Greeting: ")

    greet = greet.lower().strip(" ")

    dollar = value(greet)

    print(f"${dollar}")


def value(greeting):
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
