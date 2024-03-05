x = range(1, 1000)

num = int(input("Please enter your number: "))

divisors = []

for item in x:
    if num % item == 0:
        divisors.append(item)

print(divisors)