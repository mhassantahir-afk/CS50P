def twttr(x):
    new = ""
    for i in x:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            n = 0
        else:
            new = new + i
    return new

def main():
    word = twttr(input("Input: "))
    print("Output:", word)

main()
