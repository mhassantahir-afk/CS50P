due = 50
p = 0
c = 0

while(due>0):
    print("Amount Due:", due)
    p = int(input("Insert Coin:"))

    if p == 10 or p == 25 or p == 5:
        due = due - p
        c = c + p

print("Change Owed:", c-50)
