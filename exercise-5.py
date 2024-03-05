duplicates = []

a = [7, 15, 16, 18, 70, 78, 99]
b = [2, 13, 18, 25, 45, 58, 78, 92]

for item in a:
    if item in b:
        duplicates.append(item)

print(duplicates)