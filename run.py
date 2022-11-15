"""
Module doc string...

"randint" is a function imported from the "random" library used to help
generate 5 coordinates for the users ships.
"enum" has been imported to the enumerations of the different board states.
Class "BoardStates" contains the symbols printed on the board and what they
mean in the game.
The USER_BOARD constant contains the parameters of the user board on
which the game occurs.
"print_game_board" function prints the game board with updated boardstates
everytime user inputs valid ship guess.
"computer_ships" function randomly generated 5 coordinates that represent
the computers ships in the users board.
"user_input" function allows user to enter row and column number which it
then checks is valid.
"start_game" function then checks the users valid coordinates to see if hits
or misses a ship or has been selected before.
"""

from random import randint
import enum

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
    that represent ships that haven't been hit, but before the board is printed
    the "X" is replaced to "o" so the user doesn't know where they are.
    Every time the user selects a coordinate and misses, the "o" changes to
    "-". When they hit a ship the "o" changes to "x" to represent a hit ship.
    Both result in number of turns left to decrease by 1.
    """

    EMPTY = "o"
    SHIP_HIT = "x"
    SHIP_ALIVE = "X"
    WRONG_GUESS = "-"


# User board set up.
# All coordinates are represented with the Empty "o" BoardStates symbol.
USER_BOARD = [
    [BoardStates.EMPTY.value] * BOARD_GRID_SIZE for x in range(BOARD_GRID_SIZE)
]


def print_game_board(user_name, game_board):
    """
    Prints user board with 6 rows and 6 columns.

    The column is labelled. The BoardStates constant that is printed
    is "o" which represents empty unhit spaces. The 5 randomly
    generated ships that have the board state "X" are replaced
    with "o" before the board is printed so the user doesn't know where
    the ships are. The two parameters for this function are the game_board
    and the user_name to allow the user name to display above the board when it
    is printed.
    https://www.youtube.com/watch?v=tF1WRCrd_HQ - time of video:6:47 - This
    tutorial used to help number and label the column and row of the game board
    """

    print(f"{user_name.title()}'s BOARD:\n")
    print("     column   ")
    print("   0 1 2 3 4 5")
    print("---------------")
    row_num = 0

    for row in game_board:
        # str = " row  "
        # for i in str:
        row_to_be_printed = "|".join(row).replace(
            BoardStates.SHIP_ALIVE.value, BoardStates.EMPTY.value
        )
        # print("%s |%d |%s|" % (i, row_num, row_to_be_printed))
        print("%d |%s|" % (row_num, row_to_be_printed))
        row_num += 1
        # if row_num = (BOARD_GRID_SIZE - 1):
        #    break


def print_final_game_board(user_name, game_board):
    """
    This function is printed when the game ends.

    If the user loses it will reveal the positions of the ships they
    didn't hit with the updated key also printed so users know what
    "X" stands for. If the user wins all 5 ships will be represented
    with "x" as they hit all 5 ships.
    """
    print(f"{user_name.title()}'s FINAL BOARD:\n")
    print("     column   ")
    print("   0 1 2 3 4 5")
    print("---------------")
    row_num = 0

    for row in game_board:
        row_to_be_printed = "|".join(row)
        print("%d |%s|" % (row_num, row_to_be_printed))
        row_num += 1


def computers_ships(game_board):
    """
    Randomly generates 5 sets of ship coordinates to place on the board
    using the "randomint" function for the random library.

    If the same coordinates are selected randomly more than once the
    function uses a while loop to generate coordinates again until
    they haven't been repeated. These random coordinates are then represented
    on the game board using the BoardState enumeration for SHIP_ALIVE "X".

    https://www.youtube.com/watch?v=tF1WRCrd_HQ - time of video 11:10 -
    Youtube tutorial used to helpset up while loop to make sure random
    coordinates generated aren't the same.
    """
    for battleship in range(NO_OF_SHIPS):
        target_row = randint(0, BOARD_GRID_SIZE - 1)
        target_col = randint(0, BOARD_GRID_SIZE - 1)
        while game_board[target_row][target_col] == BoardStates.SHIP_ALIVE.value:
            target_row = randint(0, BOARD_GRID_SIZE - 1)
            target_col = randint(0, BOARD_GRID_SIZE - 1)

        game_board[target_row][target_col] = BoardStates.SHIP_ALIVE.value


def user_input():
    """
    The user inputs their guess for the row and column the ship is on.

    Validity checker for user input using Try/Except loop to check if the data
    input was an integer or if any input was given, or if the input was a
    string. An if/else if/else loop then checks if the integer input was in
    the correct range. If integer input is in the correct range it breaks out
    of the loop.
    """
    while True:
        try:
            user_guess_row = int(input("\nEnter your row here: \n"))
        except ValueError:
            print("Make sure you ENTER a row number that is an INTEGER!")
            continue
        if user_guess_row < 0:
            print("Your row number CAN'T BE A NEGATIVE NUMBER!")
            continue
        elif user_guess_row > (BOARD_GRID_SIZE - 1):
            print("Your row number CAN'T BE BIGGER THAN THE GRID SIZE!")
            continue
        else:
            break

    while True:
        try:
            user_guess_column = int(input("Enter your column here: \n"))
        except ValueError:
            print("Make sure you enter a column number that is an INTEGER!\n")
            continue
        if user_guess_column < 0:
            print("Your column number CAN'T BE A NEGATIVE NUMBER!\n")
            continue
        elif user_guess_column > (BOARD_GRID_SIZE - 1):
            print("Your column number CAN'T BE BIGGER THAN THE GRID SIZE!\n")
            continue
        else:
            break

    print(f"Your coordinate: [{user_guess_column} , {user_guess_row}]")
    return int(user_guess_row), int(user_guess_column)


def start_game():
    """
    The game function only runs if there are turns left or the user score
    hasn't reached 5. When either the number of turns left is 0 or the
    user score is 5 the start_game function doesn't run. The game is over
    and the final game board is printed.

    Checks if the user input from the user input function misses or hits the
    ships by matching it to the BoardStates constants, if the coordinate hits
    an "o" it means they missed the ship and that coordinate is replaced with
    "-" to represent a wrong guess and turns left decreases by 1. If the
    coordinate hits an "X" means they have hit a ship and this gets replaced
    with an "x" to represent a hit ship, turns left decrease by 1, and the
    user score increases by 1. If the coordinate hits a "-" or "x" it means
    they have hit this before so their turns left don't decrease. Contains
    input for user to insert their name to personalise the board when it is
    printed.

    https://www.youtube.com/watch?v=tF1WRCrd_HQ - Time of video 19:55 - Youtube
    tutorial used to help with general format of if/else-if/else loop used to
    determine the game outcome.
    """
    user_score = 0
    turns_left = 20
    print("This is a game of Battleships\n")
    # insert name to personalise user board name
    user_name = input("Enter your name here: ")
    print(f"\nHi {user_name}, get ready to play BattleShips!\n")
    print("Symbol key:\no = Empty space that hasn't been hit")
    print("x = Hit Ship")
    print("- = You hit nothing \n")

    computers_ships(USER_BOARD)
    while turns_left > 0 or user_score < 5:
        print_game_board(user_name, USER_BOARD)
        user_guess_row, user_guess_column = user_input()
        print("\n")
        if (
            USER_BOARD[user_guess_row][user_guess_column]
            == BoardStates.WRONG_GUESS.value
        ):
            print("You have already guessed this coordinate. Guess again\n")
        elif (
            USER_BOARD[user_guess_row][user_guess_column] == BoardStates.SHIP_HIT.value
        ):
            print("You have already hit this ship!\n")
        elif (
            USER_BOARD[user_guess_row][user_guess_column]
            == BoardStates.SHIP_ALIVE.value
        ):
            print("YAY, you hit a ship!\n")
            (USER_BOARD[user_guess_row][user_guess_column]) = BoardStates.SHIP_HIT.value
            turns_left -= 1
            user_score += 1
        else:
            print("AWW! you missed\n")
            (
                USER_BOARD[user_guess_row][user_guess_column]
            ) = BoardStates.WRONG_GUESS.value
            turns_left -= 1
        if user_score == 5:
            print("Congrats! you sunk all 5 ships and have won the game!\n")
            print_game_board(user_name, USER_BOARD)
            break
        print(f"User Score: {user_score}")
        print(f"You have {turns_left} turns left\n")
        if turns_left == 0:
            print("No more turns left! GAME OVER\n")
            print("Symbol Key:\no = Empty space that hasn't been hit")
            print("x = Hit Ship")
            print("- = You hit nothing")
            print("X = Ships you missed")
            print_final_game_board(user_name, USER_BOARD)
            break


if __name__ == "__main__":
    # Allows start_game function to run on a global scope.
    start_game()
