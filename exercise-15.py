# Exercise - Reverse Word Order

user_string = input("Please enter a string that has a length of 6 words or more: ")
reverse_string = []

arr = user_string.split(" ")

for x in reversed(arr):
    reverse_string.append(x)

final_reverse_string = " ".join(reverse_string)
print(final_reverse_string)