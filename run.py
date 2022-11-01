# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("This is a game of Battleships")

insert_name = input("Enter your name here: \n")
print(f"Hi {insert_name}, get ready to play BattleShips!")
        
#board set up
game_board = []

for x in range(0, 6):
    game_board.append(["0"] * 6)
    print(game_board)


