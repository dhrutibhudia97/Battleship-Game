from random import randint
import enum
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

BOARD_GRID_SIZE = 6
NO_OF_SHIPS = 5

class BoardStates(enum.Enum):
    """
    The different states the user board can take depending on the outcome.

    Enumerations are used so the different symbols printed are different
    outputs on the game function.
    When the board is initially printed all of the coordinates will be printed
    with "o" to represent empty spaces that haven't been hit. 5 of these 
    coordinates randomly selected by the computer_ships function will be "X"
    that represent that ships that havent been hit, but before the board is printed
    the "X" were replaced to "o" so user doesn't know where they are.
    Everytime the user selects a coordinates and misses, the "o" changes to "-".
    When they hit a ship the "o" changes to "x" represent a hit ship. Both result in 
    turns_left decreasing by 1.
    """
    EMPTY = "o"
    SHIP_HIT = "x"
    SHIP_ALIVE = "X"
    WRONG_GUESS = "-"

# User board set up. All coordinates are represented with the Empty "o" BoardState symbol. 
USER_BOARD = [[BoardStates.EMPTY.value] * BOARD_GRID_SIZE for x in range(BOARD_GRID_SIZE)]


def print_game_board(user_name, game_board):
    """
    Prints user board with 6 rows and 6 columns.

    The column is labelled. The BoardStates constant that is printed 
    is "o" which represents empty unhit spaces. The 5 randomly 
    generated ships which have the board state "X" are replaced 
    with "o" before board is printed so user doesn't know where 
    the ships are. The two parameters for this function are the game_board 
    and the user_name to allow users name to display above the board when it
    is printed.
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
    Randomly generates 5 sets of ship coordinates to place on the board
    using the randomint library.
    
    If the same coordinates are selected randomly more than once the 
    function uses a while loop to generates coordinates again until
    they haven't been repeated. These random coordinates are then represented
    on the game board using the BoardState enumeration for SHIP_ALIVE "X".
    """
    for target in range(NO_OF_SHIPS):
        target_row = randint(0, BOARD_GRID_SIZE - 1)
        target_col = randint(0, BOARD_GRID_SIZE - 1)
        while game_board[target_row][target_col] == BoardStates.SHIP_ALIVE.value:
            target_row = randint(0, BOARD_GRID_SIZE - 1)
            target_col = randint(0, BOARD_GRID_SIZE - 1)
	        
        game_board[target_row][target_col] = BoardStates.SHIP_ALIVE.value 



def user_input():
    """
    User inputs the row number guess for what row the ships is on the game board. 

    Validity checker for user input using Try/Except loop to check if the data
    inputed was an integer or if any input was given, or if the input was a string. 
    An if/elif/else loop then checks if the integer input was in the correct range.
    if integer input is in the correct range it breaks out of the loop and into the 
    column loop below.
    """
    while True:
        try:
            user_guess_row = int(input("\nEnter your row here: \n"))
        except ValueError:
            print("Make sure you enter a row number that is an INTEGER!")
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
        """
        User inputs the column number guess for what row the ships is on the game board. 

        Validity checker for user input using Try/Except loop to check if the data
        inputed was an integer or if any input was given, or if the input was a string. 
        An if/elif/else loop then checks if the integer input was in the correct range.
        If column integer input is in correct range it breaks out of this loop.
        """
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
    hasn't reached 5. When either the turns left is 0 or user score is 5 the
    start_game function doesn't run. The game is over and final game board is printed. 

    Checks if the users input from the user input function misses or hits the ships 
    by matching it to the BoardStates constants, if the coordinate hits an "o" it
    means they missed the ship and that coordinate is replaced with "-" to represent
    a wrong guess and turns left decreases by 1. If the coordinate hits a "X" means 
    they have hit a ship and this gets replaces with a "x" to represent a hit ship, 
    turns left decreases by 1 and user score increases by 1. If the coordinate hits 
    a "-" or "x" it means they have hit this before so their turns left doesn't decrease.
    Contains input for user to insert their name to personalise the board when it is printed.
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
        #print(USER_BOARD[user_guess_row][user_guess_column])
        if (USER_BOARD[user_guess_row][user_guess_column] == BoardStates.WRONG_GUESS.value):
            print("You have already guessed this coordinate. Guess again\n")
        elif (USER_BOARD[user_guess_row][user_guess_column] == BoardStates.SHIP_HIT.value):
            print("You have already hit this ship!\n")
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
        print(f"You have {turns_left} turns left\n")
        if turns_left == 0:
            print("No more turns left! GAME OVER\n")
            print_game_board(user_name, USER_BOARD)
            break

#Allows the game to run in a global scope.
if __name__ == "__main__":
    start_game()