# Exercise - Rock Paper Scissors

player_1 = input("What's your name? ")
player_2 = input("And you, what's your name? ")

player_1_choice = input("%s Choose between these three choices: rock, paper, or scissors? " % player_1)
player_2_choice = input("%s Choose between these three choices: rock, paper, or scissors? " % player_2)

def compare(u1, u2):
    if u1 == u2:
        print("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            print(f"{player_1} is the winner, as the choice is rock!")
        else:
            print(f"{player_2} wins the game!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            print(f"{player_1} is the winner, as the choice was scissors!")
        else:
            print(f"{player_2} wins the game!")
    elif u1 == 'paper':
        if u2 == 'rock':
            print(f"{player_1} is the winner, as the choice was paper!")
    else:
        print("Invalid input! The choice wasn't proper, try again.")

print(compare(player_1_choice, player_2_choice))