user_number = int(input("Please enter a number: "))

if user_number > 0:
    for item in range(2, user_number - 1):
        if user_number % item != 0:
            continue
        else:
            print("This number is NOT a prime number!")

elif user_number == 0:
    print("This number is NOT a prime number!")

else:
    print("This number is NOT a prime number!")1