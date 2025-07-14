def main():
    word = shorten(input("Input: "))
    print("Output:", word)


def shorten(word):
    new = ""
    for i in word:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U':
            new = new + i

    return new


if __name__ == "__main__":
    main()
