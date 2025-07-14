fr = input("Item: ")

    # fruits is a dictionary for the fruits and their calories
fruits = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherries" : "100",
    "tangerine" : "50",
    "watermelon" : "80",
}
# for capitalisation issues
fr = fr.lower()
# loop that iterates over every element in dictionary
for fruit in fruits:
    # if statment checks for valid input
    if fruit == fr:
        fr = fruits[fruit]
        print("Calories:",fr)
