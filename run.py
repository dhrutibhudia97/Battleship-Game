"""
The code for a 1 player game of battleships.

The user has to guess the location of the 5 randomly placed ships on the 6x6
game board. There are 4 different states the board can be in:
  o = Space that hasn't been hit
  x = Hit Ship
  - = You hit nothing
  X = Ships you missed
Before the board is printed to 5 ships "X" on the board is replaced with
"o" so the ship's locations remain anonymous. The user chooses the difficulty
level of the game which determines how many turns they get to guess the
coordinates of the ship. If the user inputs invalid row and column guesses they
are prompted to guess again, with a message prompting to what was wrong with
their previous guess. The Game is won by the user finding all 5 ships before
the turns run out.
"""

from random import randint
import enum

# The width and height of the game board
BOARD_GRID_SIZE = 6
# The number of ships generated and placed on the board
NO_OF_SHIPS = 5

# The symbol key to the game board
GAME_LEGEND = """
Symbol Key:
  o = Space that hasn't been hit
  x = Hit Ship
  - = You hit nothing
  X = Ships you missed
"""


class GameLevel(enum.Enum):
    """
    The different game levels for the user to pick from.

    E for EASY where the user gets 25 turns. M for Medium where the user
    gets 20 turns and H for Hard where the user gets 15 turns. The Enum has been
    imported.
    """

    E = 25
    M = 20
    H = 15


class BoardStates(enum.Enum):
    """
    The different states the user board can take depend on the outcome.

    Enumerations are used for the different symbols printed which represent
    different outputs on the game function. The Enum has been imported.
    """

    EMPTY = "o"
    SHIP_HIT = "x"
    SHIP_ALIVE = "X"
    WRONG_GUESS = "-"


# User board set up using BOARD_GRID_SIZE constant
# All coordinates are represented with the Empty "o" BoardStates symbol.
USER_BOARD = [
    [BoardStates.EMPTY.value] * BOARD_GRID_SIZE for x in range(BOARD_GRID_SIZE)
]


def print_game_board(user_name, game_board):
    """
    Prints user board in terms of BOARD_GRID_SIZE constant.

    The column is labelled. The BoardStates constant that is printed
    is "o" which represents empty unhit spaces. The 5 randomly
    generated ships that have the board state "X" are replaced
    with "o" before the board is printed so the ship's location is unknown
    to the user. The two parameters for this function are the game_board
    and the user_name to allow the user name to display above the board when it
    is printed.
    """

    print(f"{user_name.title()}'s BOARD:\n")
    print("     column   ")
    print("   0 1 2 3 4 5")
    print("---------------")
    row_num = 0
    # https://www.youtube.com/watch?v=tF1WRCrd_HQ - time of video- 6:47
    # Tutorial used to help number and label the column and row of the
    # game board
    for row in game_board:
        row_to_be_printed = "|".join(row).replace(
            BoardStates.SHIP_ALIVE.value, BoardStates.EMPTY.value
        )

        print("%d |%s|" % (row_num, row_to_be_printed))
        row_num += 1


def print_final_game_board(user_name, game_board):
    """
    This function is printed when the game ends.

    If the user loses it will reveal the positions of the ships they
    didn't hit. If the user wins all 5 ships will be represented
    with "x" as they hit all 5 ships. The parameters are the game board
    and the user name which is printed above the board.
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


def generate_and_place_random_ships(game_board):
    """
    Randomly generates 5 sets of ship coordinates to place on the board.

    The "randomint" function from the random library has been used.
    The parameter is the game_board on which the ships are placed.
    If the same coordinates are selected randomly more than once the
    function uses a while loop to generate coordinates again until
    they haven't been repeated. These random coordinates are then represented
    on the game board using the BoardState enumeration for SHIP_ALIVE "X".
    """
    for _ in range(NO_OF_SHIPS):
        ship_row = randint(0, BOARD_GRID_SIZE - 1)
        ship_col = randint(0, BOARD_GRID_SIZE - 1)
        # https://www.youtube.com/watch?v=tF1WRCrd_HQ - time of video 11:10 -
        # Youtube tutorial used to help set up while loop to make sure random
        # coordinates generated aren't the same.
        while game_board[ship_row][ship_col] == BoardStates.SHIP_ALIVE.value:
            ship_row = randint(0, BOARD_GRID_SIZE - 1)
            ship_col = randint(0, BOARD_GRID_SIZE - 1)

        game_board[ship_row][ship_col] = BoardStates.SHIP_ALIVE.value


def user_input():
    """
    The user inputs their guess for the row and column the ship is on.

    Validity checker for user input using Try/Except loop to check if the data
    input was an integer or if any input was given, or if the input was a
    string. An if/else loop then checks if the integer input was in
    the correct range. If integer input is in the correct range it is then
    inserted into the start_game function.
    """
    while True:
        try:
            user_row = int(input("\nEnter your row here: \n"))
        except ValueError:
            print("Make sure you ENTER a row number that is an INTEGER!")
            continue
        if user_row < 0:
            print("Your row number CAN'T BE A NEGATIVE NUMBER!")
            continue
        elif user_row > (BOARD_GRID_SIZE - 1):
            print("Your row number CAN'T BE BIGGER THAN THE GRID SIZE!")
            continue
        else:
            break

    while True:
        try:
            user_column = int(input("Enter your column here: \n"))
        except ValueError:
            print("Make sure you enter a column number that is an INTEGER!\n")
            continue
        if user_column < 0:
            print("Your column number CAN'T BE A NEGATIVE NUMBER!\n")
            continue
        if user_column > (BOARD_GRID_SIZE - 1):
            print("Your column number CAN'T BE BIGGER THAN THE GRID SIZE!\n")
            continue
        break

    print(f"Your coordinate: [{user_column} , {user_row}]")
    return int(user_row), int(user_column)


def get_game_level():
    """
    Gives the user a choice of playing an easy(E), medium(M), or hard(H) game.

    This determines the number of turns the user gets in the game.
    E = 25. M = 20. H = 15. The ships are in 5 of the possible 36 locations
    on the game grid.
    """
    game_level_choice = None
    while True:
        print("Do you want to play an EASY(E), MEDIUM(M) or HARD(H) game?")
        game_level_choice = input("Enter either E | M | H: ").upper()
        if game_level_choice not in ("E", "M", "H"):
            print("\nPlease enter E or M or H to choice game level")
            continue
        else:
            break

    return game_level_choice


def start_game():
    """
    The start game function only runs if there are turns left or hasn't won.

    When either the number of turns left is 0 or the user score is 5 the
    start_game function doesn't run. The game is over and the final game board
    is printed. Checks if the user input from the user input function misses
    or hits the ships by matching it to the BoardStates constants, if the
    coordinate hits an "o" it means they missed the ship and that coordinate
    is replaced with "-" to represent a wrong guess and turns left decreases by
    1. If the coordinate hits an "X" means they have hit a ship and this gets
    replaced with an "x" to represent a hit ship, turns left decrease by 1, and
    the user score increases by 1. If the coordinate hits a "-" or "x" it
    means they have hit this before so their turns left don't decrease.
    Contains input for user to insert their name to personalise the board when
    it is printed.
    """

    print("This is a game of Battleships\n")
    # insert the user's name to personalise the game board.
    user_name = input("Enter your name here: ")
    print(f"\nHi {user_name.capitalize()}, get ready to play BattleShips!\n")

    game_level = get_game_level()

    print(GAME_LEGEND)

    user_score = 0
    turns_left = GameLevel[game_level].value
    print(f"You have {turns_left} turns left\n")

    generate_and_place_random_ships(USER_BOARD)

    while turns_left > 0 or user_score < 5:
        print_game_board(user_name, USER_BOARD)
        user_row, user_column = user_input()
        print("\n")
        # https://www.youtube.com/watch?v=tF1WRCrd_HQ - Time of video 19:55 -
        # Youtube tutorial used to help with the general format of if/else-if/else
        # loop used to determine the game outcome.
        if USER_BOARD[user_row][user_column] == BoardStates.WRONG_GUESS.value:
            print("You have already guessed this coordinate. Guess again\n")
        elif USER_BOARD[user_row][user_column] == BoardStates.SHIP_HIT.value:
            print("You have already hit this ship!\n")
        elif USER_BOARD[user_row][user_column] == BoardStates.SHIP_ALIVE.value:
            print("YAY, you hit a ship!\n")
            USER_BOARD[user_row][user_column] = BoardStates.SHIP_HIT.value
            turns_left -= 1
            user_score += 1
        else:
            print("AWW! you missed\n")
            USER_BOARD[user_row][user_column] = BoardStates.WRONG_GUESS.value
            turns_left -= 1
        if user_score == 5:
            print("Congrats! you sunk all 5 ships and have won the game!\n")
            print_game_board(user_name, USER_BOARD)
            break
        print(f"User Score: {user_score}")
        print(f"You have {turns_left} turns left\n")
        if turns_left == 0:
            print("No more turns left! GAME OVER\n")
            print(GAME_LEGEND)
            print(f"You Hit {user_score}/5 Battleships\n")
            print_final_game_board(user_name, USER_BOARD)
            break


# Allows start_game function to run on a global scope
if __name__ == "__main__":
    start_game()
