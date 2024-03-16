# Exercise - Draw A Game Board

    # function - used to create the horizontal lines of the game board
def horizontal_line():
    print(" --- " * board_size)

    # function - used to create the vertical lines of the game board
def vertical_line():
    print("|  " * (board_size + 1))

board_size = int(input("What size of game board? "))

for index in range(board_size):
    horizontal_line()
    vertical_line()

print(horizontal_line())