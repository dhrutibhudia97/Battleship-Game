from random import randint
import enum
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

BOARD_GRID_SIZE = 6
NO_OF_SHIPS = 5

class BoardStates(enum.Enum):
    EMPTY = "o"
    SHIP_HIT = "x"
    SHIP_ALIVE = "X"
    WRONG_GUESS = "-"

# user board set up
USER_BOARD = [[BoardStates.EMPTY.value] * BOARD_GRID_SIZE for x in range(BOARD_GRID_SIZE)]
# hidden computer board
#COMPUTERS_BOARD = [[" "] * BOARD_GRID_SIZE for y in range(BOARD_GRID_SIZE)]
# .replace and . split are not working to remove comma so used this method instead
# function to see the board
def print_game_board(user_name, game_board):
    print(f"{user_name}'s BOARD:")
    print('   0 1 2 3 4 5')
    print('---------------')
    row_num = 0
    for row in game_board:
        row_to_be_printed = "|".join(row).replace(
            BoardStates.SHIP_ALIVE.value, BoardStates.EMPTY.value
        )
        #print("%d |%s|" % (row_num, "|".join(row)))
        print("%d |%s|" % (row_num, row_to_be_printed))
        row_num += 1
#print_game_board(USER_BOARD)
#print("\n")

#def print_computer_board(game_board):
 #   print('COMPUTER BOARD: ')
  #  print('   0 1 2 3 4 5')
   # print('---------------')
    #row_num = 0
    # computer hidden game board
    #for row in game_board:
     #   print("%d |%s|" % (row_num, "|".join(row)))
      #  row_num += 1
#print_computer_board(COMPUTERS_BOARD)


#get computer random generated ship location
def computers_ships(game_board):
    for target in range(NO_OF_SHIPS):
        target_row = randint(0, BOARD_GRID_SIZE - 1)
        target_col = randint(0, BOARD_GRID_SIZE - 1)
        while game_board[target_row][target_col] == BoardStates.SHIP_ALIVE.value:
            target_row = randint(0, BOARD_GRID_SIZE - 1)
            target_col = randint(0, BOARD_GRID_SIZE - 1)
	        # target_row, target_col = user_input()
        game_board[target_row][target_col] = BoardStates.SHIP_ALIVE.value 
# NEED TO ADD THESE AS VALIDITY CHECKERS
# user needs to input data
# users guess is stored so they can't guess same numbers again
# invalid user input/error options if (1)Not an integer (is.digit...?)
# elif (2) Integer not in range. else(3)Guessed that integer combo already
# print user prompt message

# asks users what row and column to guess battleship is in
def user_input():
    print("\nCoordinates should be a number between 0 - 5.")
    print("Example:[3, 5] \n")
    user_guess_column = input("Enter your row here: ")
    while user_guess_column not in '012345':
        print("Column coordinate not an integer. Input a number between 0-5")
        user_guess_column = input("Enter your row here: ")
    user_guess_row = input("Enter your column here: ")
    while user_guess_row not in '012345':
        print("Row coordinate not valid, try again")
        user_guess_row = input(("Enter your column here: "))
    print(f"Your coordinate: [{user_guess_row} , {user_guess_column}]")
    #print(f"Your coordinate: [{user_guess_column} , {user_guess_row}]")
    return int(user_guess_row), int(user_guess_column)


# game function, only runs if there are user turns left and ships left to hit.
#computers_ships(COMPUTERS_BOARD)
#print_game_board(COMPUTERS_BOARD)
def start_game():
    user_score = 0
    turns_left = 20
    print("This is a game of Battleships")
    # insert name to personalise user board name
    user_name = input("Enter your name here: \n")
    print(f"Hi {user_name}, get ready to play BattleShips!")
    print('\n')

    computers_ships(USER_BOARD)
    while turns_left > 0 or user_score < 5:
        print("Welcome to the game")
        print_game_board(user_name, USER_BOARD)
        user_guess_column, user_guess_row = user_input()
        print('\n')
        print(USER_BOARD[user_guess_column][user_guess_row])
        if USER_BOARD[user_guess_column][user_guess_row] in (
            BoardStates.SHIP_HIT, BoardStates.WRONG_GUESS):
            print("You have already guessed this coordinate. Guess again")
        elif (USER_BOARD[user_guess_column][user_guess_row] == BoardStates.SHIP_ALIVE.value):
            print("YAY, you hit a ship!")
            USER_BOARD[user_guess_column][user_guess_row] = BoardStates.SHIP_HIT.value
            turns_left -= 1
            user_score += 1
        else:
            print("AWW! you missed")
            USER_BOARD[user_guess_column][user_guess_row] = BoardStates.WRONG_GUESS.value
            turns_left -= 1
        if user_score == 5:
            print("Congrats! you sunk all 5 ships and have won the game!")
            print_game_board(user_name, USER_BOARD)
            break
        print(f"User Score: {user_score}")
        print(f"You have {turns_left} turns left")
        if turns_left == 0:
            print("No more turns left! GAME OVER")
            print_game_board(user_name, USER_BOARD)
            break


if __name__ == "__main__":
    start_game()