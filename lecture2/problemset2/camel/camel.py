def camelcase(x):
    letters = ""
    for i in x:
        if i.isupper() == True:
            letters = letters + "_" + i.lower()
        else:
            letters = letters + i
    return letters

def main():
    t = camelcase(input("camelCase: "))
    print("snake_case: ", t)

main()
