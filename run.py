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

# function to see the board
def print_game_board(user_name, game_board):
    """
    Prints user board with 6 rows and 6 columns.

    The column is labelled. The BoardStates constant that is printed 
    is "o" which represents empty unhit spaces. The 5 randomly 
    generated ships which have the board state "X" are replaces 
    with "o" before board is printed so user doesn't know where 
    the ships are.
    """
    print(f"{user_name}'s BOARD:\n")
    print('     column   ')
    print('   0 1 2 3 4 5')
    print('---------------')
    row_num = 0
    
    for row in game_board:
        #str = " row  "
        #for i in str:
            row_to_be_printed = "|".join(row).replace(
                BoardStates.SHIP_ALIVE.value, BoardStates.EMPTY.value
        )
            #print("%s |%d |%s|" % (i, row_num, row_to_be_printed))
            print("%d |%s|" % (row_num, row_to_be_printed))
            row_num += 1
            #if row_num = (BOARD_GRID_SIZE - 1):
            #    break
            

#get computer random generated ship location
def computers_ships(game_board):
    """
    Randomly generates 5 sets of ship coordinates to place on the board.
    
    If the same coordinates 
    selected randomly more then once the function just generates 
    coordinates again.
    """
    for target in range(NO_OF_SHIPS):
        target_row = randint(0, BOARD_GRID_SIZE - 1)
        target_col = randint(0, BOARD_GRID_SIZE - 1)
        while game_board[target_row][target_col] == BoardStates.SHIP_ALIVE.value:
            target_row = randint(0, BOARD_GRID_SIZE - 1)
            target_col = randint(0, BOARD_GRID_SIZE - 1)
	        
        game_board[target_row][target_col] = BoardStates.SHIP_ALIVE.value 


# asks users what row and column to guess battleship is in
def user_input():
    """
    User inputs there row and column number.

    Validity checker, to check if the data inputed was an integer.
    This also checks if an inout was given and if it were a string it 
    just asks user again. It then checks in integer input was in range.
    """
    while True:
        try:
            user_guess_row = int(input("\nEnter your row here: \n"))
        except ValueError:
            print ("Make sure you enter a row number that is an INTEGER!")
            continue
        if user_guess_row < 0:
            print("Your row number CANNOT BE A NEGATIVE NUMBER!")
            continue
        elif user_guess_row > (BOARD_GRID_SIZE -1):
            print("Your row number CANNOT BE BIGGER THAN THE GRID SIZE!")
            continue
        else:
            break


    while True:
        try:
            user_guess_column = int(input("Enter your column here: \n"))
        except ValueError:
            print ("Make sure you enter a column number that is an INTEGER!")
            continue
        if user_guess_column < 0:
            print("Your column number CANNOT BE A NEGATIVE NUMBER!")
            continue
        elif user_guess_column > (BOARD_GRID_SIZE -1):
            print("Your column number CANNOT BE BIGGER THAN THE GRID SIZE!")
            continue
        elif user_guess_column is None:
            print("You have to ENTER A NUMBER!")
            continue
        else:
            break
    

    print(f"Your coordinate: [{user_guess_column} , {user_guess_row}]")
    return int(user_guess_row), int(user_guess_column)


# game function, only runs if there are user turns left and ships left to hit.
def start_game():
    """
    The game function that only runs if there are turns left or the user score 
    hasn't reached 5.

    Checks if the users input misses or hits the ships. Or has already been given.
    Contains input for user to insert their name to personalise the board.
    """
    user_score = 0
    turns_left = 20
    print("This is a game of Battleships")
    # insert name to personalise user board name
    user_name = input("Enter your name here: \n")
    print(f"Hi {user_name}, get ready to play BattleShips!")
    print('\n')

    computers_ships(USER_BOARD)
    while turns_left > 0 or user_score < 5:
        print_game_board(user_name, USER_BOARD)
        user_guess_row, user_guess_column = user_input()
        print('\n')
        print(USER_BOARD[user_guess_row][user_guess_column])
        if (USER_BOARD[user_guess_row][user_guess_column] == BoardStates.WRONG_GUESS.value):
            print("You have already guessed this coordinate. Guess again")
        elif (USER_BOARD[user_guess_row][user_guess_column] == BoardStates.SHIP_HIT.value):
            print("You have already hit this ship! \n")
            turns_left = turns_left
            user_score = user_score
        elif (USER_BOARD[user_guess_row][user_guess_column] == BoardStates.SHIP_ALIVE.value):
            print("YAY, you hit a ship!\n")
            (USER_BOARD[user_guess_row][user_guess_column]) = BoardStates.SHIP_HIT.value
            turns_left -= 1
            user_score += 1
        else:
            print("AWW! you missed\n")
            (USER_BOARD[user_guess_row][user_guess_column]) = BoardStates.WRONG_GUESS.value
            turns_left -= 1
        if user_score == 5:
            print("Congrats! you sunk all 5 ships and have won the game!\n")
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