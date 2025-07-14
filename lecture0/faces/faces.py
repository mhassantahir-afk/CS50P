# first i will have a variable that can take input for a string with emoji
statement = str(input("Enter a line with a face emoji:\n"))

# now ill take the variable and use the replace function(i read it on the documentation)
new_statement = statement.replace(":)", "🙂").replace(":(", "🙁")

# now ill put a print function
print(new_statement)
