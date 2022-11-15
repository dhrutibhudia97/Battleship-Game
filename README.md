## REMINDER ##
* Your dependencies must be placed in the `requirements.txt` file

# BATTLESHIP GAME

The BattleShip game is a game in the python terminal run using Heroku.
The aim of this game is for users to try and find the computers' 5 battleships on the game board by guessing the coordinates correctly in 20 turns or under. 
The board grid size is (6x6), 36 spaces and each of the 5 battleships takes up 1 space.
The purpose of this game is to entertain the user with minimal knowledge needed beforehand as the outcome of the game is based off luck. It is easy for anyone to play, no other player is needed and they just need to guess a row and column number. They have to guess where the 5 ships are before their turns run out. The target audience is anyone is wants to play a game against the computer.

![python responsive screen design](https://user-images.githubusercontent.com/107180641/201770085-acfe3871-bb03-4f19-a97a-7cf4ee732a7e.png)


## The Rules Of The Game

Battleships game is based on a 2 player board game in which users take turns to guess where the ship is on their game board and if they guess correctly they destroy the ship. More info about this game can be found here: https://en.wikipedia.org/wiki/Battleship_(game)

This game varies slightly by firstly being 1 player so the user is just guessing where the computer's ships are.
The different symbols of the board represent the different states the locations on the board can be in.

- Initially, the board is printed, and all positions are filled with "o" which represents an empty space that can be hit.
- Once the users guess a valid row and column number, this coordinate on the board is checked to see if that position is empty in which case the "o" turns to "-" representing a wrong guess. 
- If the location they hit has a ship the "o" turns into "x" which represents a ship that has been hit.
- To win this game the user needs to hit all 5 computer ships and get 5 "x" on their board before their 20 turns are finished.


## Features

### Existing Feature

#### Random Coordinate Generator
- The computer generates 5 random coordinates to place ships on the game board using the random library that has been imported.
- The user cannot see where the ships have been placed as the symbols for the ships have been replaced with the symbol for empty before the board is printed.

[insert screenshot of board before input given]

#### The User Input Validator 
- The row and column number input is checked to see if any data has been inputted, then checking to see if it is an integer. If it isn't an integer then the user is asked to input the row or column number again.
- If it is an integer it is checked to see if it is a positive number and if it is smaller than the board grid size. If it isn't the user is asked to input the row or column number again.
[insert screenshot of entering nothing/float/string/negative integer and too big an integer]

#### The Game Function Validator
- User inserts name which will be printed on top of the game board for each round.
- The same coordinates cannot be entered again. If it has, the turns left and the user score doesn't change. The user is told they have already hit this location and asked to insert another value.
- If the coordinate hasn't been entered before, it is checked to see if it hits or misses a ship, deducting 1 from turns left and adding 1 to the user score accordingly.
- The game function stops running when either there are 0 turns left or the user score is 5. The last game is printed and the game ends.

[insert screenshot or a hit]
[miss ship ]
[already hit ship]
[already missed location.]
[insert screenshot of either hitting all ships and winning the game]
[losing game by not hitting all ships.]

#### The User Coordinates Are Saved For Each Round Of The Game.
 

### Future Features
- Allow it to be a 2-player game with the computer randomly guessing coordinates to hit users' ships.
- Allow various battleship sizes to take up more than one coordinate space.


## Data Model

A grid is created that represents the user's board. It holds the 5 randomly generated ships. With each turn, the user's board holds the data of the previous coordinates picked, the location of the ships, and the user's current score and turns left. 
The class "BoardStates" is used which contains enumerations for the different states each position of the board can be: Empty, Alive ships, Hit ships, and Missed guesses.


## Testing
- I have manually checked that the user's inputs are valid before the game function runs. When the user's row or column input is: blank, a string, float, a negative integer, or an integer bigger than 5 the user is prompted to enter another input.
- I have tested that the user's inputs in the game function affect the user's score and the number of turns left correctly. If the same coordinate is selected this has no effect on the turns left or the user score.

- Test game outputs on Heroku terminal... i.e game stops if no turns left or 5 is scored...######
- - PEP8 linter ####


## Testing Features
|Feature being tested                | How it was manually tested           | Results                     |
|------------------------------------|--------------------------------------|-----------------------------|
|User validation function excepting incorrect input type| Entered nothing, string and floats   | ✓ User asked to enter an integer|
|User validation function excepting number in in the board size range | Entering negative integers and integers > 5 | ✓ Message printed to tell user they cannot enter negative values or numbers bigger then the board size |
| Start game function not decreasing turns left if the same wrong guess coordinate has been selected| Entering the same coordinates for a missed guess| ✓ Message printed telling user they have already guessed that coordinate and to try again|
| Start game function not increasing user score multiple times if same ship is hit| Entering same coordinates for a known ship location| ✓ Message shows telling user they have already hit this ship and to guess again. User score does not increase and the number of turns left does not decrease| 
|Start game function when user loses game| Entering 20 coordinate guesses and not hitting 5 ships | ✓ Results in message telling user they lost game and they have 0 turns left |
|Start game function when user wins game | Entering coordinates and hitting all 5 ships before turns left = 0 | ✓ Results in message congratulating user and telling them they hit all 5 ships and have won the game.| 
| Testing codes format | PEP8 linter / running "black run.py" and "pycodestyle" | No major issues. Some code lines are longer than 80 characters but cannot be shorted otherwise it compromises the codes functionality|
| Testing the game format on the Heroku terminal | Deploying battleships game on Heroku terminal | ✓ The game work and can be played on this platform with no errors|



### Bugs

#### Resolved Bugs
- Forgot the rows were indexed so kept getting errors that it was out of range, I needed to decrease the range for BOARD_GRID_SIZE to (BOARD_GRID_SIZE -1).
- Selecting the same coordinates kept increasing the user score and decreasing turns left. I added extra if/else-if statements to the state_game function that prompted the user to input a row or column number they haven't picked before if they hit a "-" or "x" on the board.

#### Unresolved Bugs
- Label the rows of the grid by spelling "row" vertically next to the row numbers. Tried using "print("%s |%d |%s|" % (i, row_num, row_to_be_printed))" where "i" represented each letter in the string "row" but this just printed the table 6 times. So I have labelled the column but not the row.


### Future Features
Make the game 2-player and add a computer board that allows the computer to guess coordinates on the user board and vice versa.


## Deployment
##HAVEN'T FORKED/CLONED REPOSITORY##

Steps for deployment:
1) On Heroku dashboard selected "create new app"
2) Add Buildpacks:
    - python
    - nodejs
3) Add Config Vars:
    - KEY: PORT
    - VALUE: 8000
4) Linked the Heruko app to the GitHub repository "Battleship-Game"
5) Clicked on "Manually Deploy"

https://battleship-game-db.herokuapp.com/




## Credits
- For helping make the grid layout for the USER_BOARD
    - https://www.youtube.com/watch?v=7Ki_2gr0rsE&ab_channel=DylanIsrael 
- For help with the initial template used to make sure user input was valid.
    - Love Sandwiches module from Code Institute 	
- To label the column and number of row of the grid. Also for idea to use while loop when randomly generating ship coordinates to not get any repeats. Idea for general if/else-if/else loop used in game function.
    - https://www.youtube.com/watch?v=tF1WRCrd_HQ&ab_channel=KnowledgeMavens - 
- For ideas about adding constants for grid size and the number of ships. Also for the idea of enumerations for the different board states.
    - Mentor Sandeep Aggarwal
- For converting input into integers.
    - https://pynative.com/python-check-user-input-is-number-or-string/#:~:text=To%20check%20if%20the%20input%20string%20is%20an%20integer%20number,using%20the%20int()%20constructor.&text=To%20check%20if%20the%20input%20is%20a%20float%20number%2C%20convert,using%20the%20float()%20constructor.
