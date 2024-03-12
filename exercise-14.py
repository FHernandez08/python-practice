# Exercise - List Remove Duplicates

list1 = [1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]

no_duplicates = []

for x in list1:
    if not no_duplicates:
        no_duplicates.append(x)
    else:
        if x in no_duplicates:
            continue
        else:
            no_duplicates.append(x)

print(no_duplicates)