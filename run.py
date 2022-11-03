# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("This is a game of Battleships")

insert_name = input("Enter your name here: \n")
print(f"Hi {insert_name}, get ready to play BattleShips!")
        
#board set up
game_board = []

#need to fix grid layout so each row is on a new line
for row in range(0,6):
    game_board.append(["O"] *6)

def print_game_board(game_board):
    for row in game_board:
        print(row)

print_game_board(game_board)


