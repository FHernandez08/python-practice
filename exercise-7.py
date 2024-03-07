# Exercise - List Comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_years = [item for item in a if item % 2 == 0] # for is used to loop through the list and uses an if statement to determine the item if it fits the condition
print(even_years)