import random

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("This is a game of Battleships")

insert_name = input("Enter your name here: \n")
print(f"Hi {insert_name}, get ready to play BattleShips!")
        
# board set up
game_board = []

# need to fix grid layout so comma,quotes and 
# inner square brackets
# are removed. 
# .replace and . split are not working!
for row in range(0, 6):
    game_board.append(["O"] * 6)
    

def print_game_board(game_board):
    for row in game_board:
        print(row)


print_game_board(game_board)


# function to randomly generate computers guess
# random row and ran column number (between 1-6).abs

def computer_row_guess(game_board):
    return random.randint(0, 5)

def computer_col_guess(game_board):
    return random.randint(0, 5)


print(f"Computer guessed coordinates: [{computer_row_guess(game_board)}, {computer_col_guess(game_board)}]")

# Store computers guess 
computer_ship_row = computer_row_guess(game_board)
computer_ship_col = computer_col_guess(game_board)

# win - function first to hit all 5
# count-down function - user has 20 goes at guessing (20/36 to find 5...)

# User inputs there guess
# row and column number (between 1-6)
# users guess is stored so they can't guess same numbers again
# invalid user input/error options if (1)Not an integer 
# elif (2) Integer not in range. else(3)Guessed that integer combo already

# print user prompt message
print("\nCoordinates should be 2 numbers seperated by a comma. A number between 0 - 5")
print("Example:[3, 5] \n")

#user_guess = (f"[{input('Enter your row here: ')} , {input('Enter your column here: ')}]")
user_guess_row = input('Enter your row here: ')
user_guess_column = input('Enter your column here: ')
print(f"[{user_guess_row} , {user_guess_column}]")

if user_guess_row.isdigit() and user_guess_column.isdigit(): #tried adding and in range(5)... didn't work
    print('Provided value is an integer in the correct range')
    #user_guess = int(integer)
    #print(user_guess)
else:
    if (user_guess_row > range(5)) or (user_guess_column > range(5)):
        print ("That coordinate is not on the grid.")
    else:
        print('Provided value is not an integer')
        #continue not properly in loop

 #   try:
  #      [int(value) for value in values]
   #     if len(values) != 2:
    #        raise ValueError(
      #          f"Exactly 6 values required, you provided {len(values)}"
     #       )
      #      elif 
    #except ValueError as e:
     #   print(f"Invalid data: {e}, please try again.\n")
      #  return False

   # return True

if user_guess_row == computer_ship_row and user_guess_column == computer_ship_col:
    print("Congratulations you hit my battleship :D")
else:
    print("Aww, you missed my battleship! :(")
    game_board[int(user_guess_row)][int(user_guess_column)] = "X"
    print_game_board(game_board)



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


