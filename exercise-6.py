string = input("Please enter a string: ")

string = str(string)
reversedString = string[::-1]

print(reversedString)

if string == reversedString:
    print("This word is a palindrome")
else:
    print("This word is NOT a palindrome")