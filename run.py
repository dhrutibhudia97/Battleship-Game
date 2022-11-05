from random import randint

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("This is a game of Battleships")

insert_name = input("Enter your name here: \n")
print(f"Hi {insert_name}, get ready to play BattleShips!")

# user board set up
USER_BOARD = []

# hidden computer board
COMPUTERS_BOARD = []

# need to fix grid layout so comma,quotes and
# inner square brackets
# are removed.
# .replace and . split are not working!
for row in range(0, 6):
    USER_BOARD.append(["O"] * 6)
    
print('\n')

def print_user_board(USER_BOARD):
    print(f"{insert_name}'s BOARD: ")
    print('   0 1 2 3 4 5')
    print('---------------')
    row_num = 0
    for row in USER_BOARD:
        print("%d |%s|" % (row_num, "|".join(row)))
        row_num += 1

print_user_board(USER_BOARD)

print("\n")


# computer hidden game board
for row in range(0, 6):
    COMPUTERS_BOARD.append(["*"] * 6)

def print_computer_board(COMPUTERS_BOARD):
    print('COMPUTER BOARD: ')
    print('   0 1 2 3 4 5')
    print('---------------')
    row_num = 0
    for row in COMPUTERS_BOARD:
        print("%d |%s|" % (row_num, "|".join(row)))
        row_num += 1

print_computer_board(COMPUTERS_BOARD)


# function to randomly generate computers guess
# random row and ran column number (between 1-6).abs

#get computer random generated ship location
def computers_ships(COMPUTERS_BOARD):
    for ship in range(5):
        computer_row = randint(0,6)
        computer_col = randint(0,6)
        while COMPUTERS_BOARD[computer_row][computer_col] == "X":
            computer_row = randint(0,6)
            computer_col = randint(0,6)
        COMPUTERS_BOARD[computer_row][computer_col] = "X"


# 
#print_computer_board(COMPUTERS_BOARD)
#print(f"Computer guessed coordinates: [{computer_row_guess(USER_BOARD)}, {computer_col_guess(USER_BOARD)}]")

#print(computer_guesses(USER_BOARD))

# Store computers guess
#computer_ship_row = computer_row_guess(USER_BOARD)
#computer_ship_col = computer_col_guess(USER_BOARD)

# win - function first to hit all 5
# count-down function - user has 20 goes at guessing (20/36 to find 5...)

# User inputs there guess
# row and column number (between 1-6)
# users guess is stored so they can't guess same numbers again
# invalid user input/error options if (1)Not an integer
# elif (2) Integer not in range. else(3)Guessed that integer combo already

# print user prompt message
print("\nCoordinates should be 2 numbers (between 0 - 5) seperated by a comma.")
print("Example:[3, 5] \n")

# user_guess = (f"[{input('Enter your row here: ')} , {input('Enter your column here: ')}]")
def user_input():
    user_guess_row = input("Enter your row here: ")
    user_guess_column = input("Enter your column here: ")
    print(f"[{user_guess_row} , {user_guess_column}]")
    return int(user_guess_row), int(user_guess_column)

    #if (
       # user_guess_row.isdigit() and user_guess_column.isdigit()):  
        # tried adding and in range(5)... didn't work
     #   print("Provided value is an integer")
      #  while user_guess_row > 6:
       #     print("Please enter valid row number between 0 - 5")
        #    user_guess_row = input("Enter your row here: ")
    #    while user_guess_column > 6:
     #       print("Please enter valid column number between 0 - 5")
      #      user_guess_column = input("Enter your column here: ")
       # return int(user_guess_row), int(user_guess_column)
        #print(f"{user_guess_row}, {user_guess_column}")

user_input()
    # if int(user_guess_row) > 5 and int(user_guess_column) > 5:
    #    print("number is not on the grid")
    # user_guess = int(integer)
    # print(user_guess)
    #if (user_guess_row) or (user_guess_column): #> not supported between str and int
     #   print("That coordinate is not on the grid.")
#else:
#    print("Provided value is not an integer")
    # continue not properly in loop

#   try:
#      [int(value) for value in values]
#     if len(values) != 2:
#        raise ValueError(
#          f"Exactly 6 values required, you provided {len(values)}"
#       )
#      elif
# except ValueError as e:
#   print(f"Invalid data: {e}, please try again.\n")
#  return False

# return True

#if user_guess_row == computer_ship_row and user_guess_column == computer_ship_col:
 #   print("Congratulations you hit my battleship :D")
#else:
 #   print("Aww, you missed my battleship! :(")
   # USER_BOARD[int(user_guess_row)][int(user_guess_column)] = "X"
  #  print_user_board(USER_BOARD)


#score tally
def user_score(board):
    score = 0
    for row in board:
        for column in row:
            if column == "X"@
            score += 1
    return score

# similar to switch case... get user results...
# if computer_guess == user guess
#   print("congrats... you hit s ship")
#   user score = += 1
#   user_goes_left -=1

# elif computer guess == previous user guess
# print (you have already hit this spot...)

# elif user score == 5
# print (congrats, you blew up all of their ships...you win)
# break out of loop.

# else computer guess != user guess
#     print("YOU MISSED")
#     user_goes_left -=1
