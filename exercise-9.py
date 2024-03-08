# Exercise - Guessing Game One

import random

number_chosen = random.randint(1, 10)

guess = 0

while guess != number_chosen:
    guess = int(input("Please enter a number from 1 to 9: "))

    if guess < number_chosen:
        print("Too low of a guess, please try again!")
    elif guess > number_chosen:
        print("Too high of a guess, please try again!")
    else:
        print("Your guess is correct!")