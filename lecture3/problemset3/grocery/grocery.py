#declaring dictionary for list of food items
food_list = {}
# loop runs until EOF error
while True:
    try:
        # takes input from user for item
        food = input()
        # if food is already in dict then we simply add to int value associated
        if food in food_list:
            food_list[food] += 1
        # else we add new value starting with 1
        else:
            food_list[food] = 1
    except(EOFError):
        print("\n")
        break
# sorts dict alphabetically
food_list = dict(sorted(food_list.items(), key=lambda item: item[0]))
# prints in required format
for i in food_list:
    print(food_list[i], i.upper())
