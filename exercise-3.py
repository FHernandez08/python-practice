arr = [7, 16, 26, 35, 57, 66, 73, 75, 88, 97]

newArr = []

for element in arr:
    if element < 81:
        newArr.append(element)
    else:
        print("The element is too big!")

print(newArr)