import random

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("This is a game of Battleships")

insert_name = input("Enter your name here: \n")
print(f"Hi {insert_name}, get ready to play BattleShips!")
        
# board set up
game_board = []

# need to fix grid layout so comma,quotes and inner square brackets are removed. 
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
    return random.randint(0, 6)

def computer_col_guess(game_board):
    return random.randint(0, 6)

print(computer_row_guess(game_board))
print(computer_col_guess(game_board))

# win - function first to hit all 5
# count-down function - user has 20 goes at guessing (20/36 to find 5...)

# User inputs there guess
# row and column number (between 1-6)
# users guess is stored so they can't guess same numbers again
# invalid user input/error options if (1)Not an integer 
# elif (2) Integer not in range. else(3)Guessed that integer combo already




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


