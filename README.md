# BATTLESHIP GAME

The BattleShip game is a game in the python terminal run using Heroku.
The aim of this game is for users to try and find the computers' 5 battleships on the game board by guessing the coordinates correctly before
their number of turns left runs out.
Users are given an option at the beginning of the game to pick easy/ medium
or hard. This determines how many turns they get: easy - 25, medium - 20, and hard - 15.
The board grid size is (6x6), 36 spaces and each of the 5 battleships takes up 1 space.
The purpose of this game is to entertain the user with no prior knowledge needed as the outcome of the game is based on luck. It is easy for anyone to play, no other player is needed and they just need to guess a row and column number. They have to guess where the 5 ships are before their turns run out. The target audience is anyone who wants to play a small game on the computer by themselves.

![python responsive screen design](https://user-images.githubusercontent.com/107180641/202027634-12ee1d6e-e589-439e-938c-09522f8784db.png)


## The Rules Of The Game

Battleships game is based on a 2 player board game in which users take turns to guess where the ship is on their game board and if they guess correctly they destroy the ship. More info about this game can be found here: https://en.wikipedia.org/wiki/Battleship_(game)

This game varies slightly by firstly being 1-player so the user is just guessing where the computer's ships are.
The different symbols on the board represent the different states the locations on the board can be in.

- Initially, the board is printed, and all positions are filled with "o" which represents a space that can be hit.
- Once the users guess a valid row and column number, this coordinate on the board is checked to see if that position is empty in which case the "o" turns to "-" representing a wrong guess. 
- If the location they hit has a ship the "o" turns into "x" which represents a ship that has been hit.
- To win this game the user needs to hit all 5 computer ships and get 5 "x" on their board before their 20 turns are finished.


## Features

### Existing Feature

#### Inserting user name
- The user inserts their name which is then used to name the game board.

![insert user name](https://user-images.githubusercontent.com/107180641/202028072-2c106186-65e5-4c2b-8b53-c2cf17f0cdc6.png)

#### Game difficulty choice
- The user gets the choice at the beginning of the game Easy/Medium/Hard. This
determines how many turns they get to guess the location of the ships.

![game difficulty choice](https://user-images.githubusercontent.com/107180641/202028254-5a9a71e2-ccd0-4d12-af5c-07fe512960c5.png)

#### Random Coordinate Generator
- The computer generates 5 random coordinates to place ships on the game board using the random library that has been imported.
- The user cannot see where the ships have been placed as the symbols for the ships have been replaced with the symbol for empty before the board is printed.

![first board printed](https://user-images.githubusercontent.com/107180641/202028444-06b3f975-eaa1-47a1-b541-5f771d2865d7.png)

#### The User Input Validator 
- The row and column number input is checked to see if any data has been inputted, then checking to see if it is an integer. If it isn't an integer then the user is asked to input the row or column number again.
- If it is an integer it is checked to see if it is a positive number and if it is smaller than the board grid size. If it isn't the user is asked to input the row or column number again.

![incorrect user input](https://user-images.githubusercontent.com/107180641/202028730-8056180b-66e7-4023-b91f-67161d5c9f62.png)

![correct user input](https://user-images.githubusercontent.com/107180641/202028942-b90f9a82-9c8a-4217-a4e6-ebc2df04bf3b.png)

#### The Game Function Validator
- User inserts name which will be printed on top of the game board for each round.
- The same coordinates cannot be entered again. If it has, the turns left and the user score doesn't change. The user is told they have already hit this location and asked to insert another value.
- If the coordinate hasn't been entered before, it is checked to see if it hits or misses a ship, deducting 1 from turns left and adding 1 to the user score accordingly.
- The game function stops running when either there are 0 turns left or the user score is 5. The last game is printed and the game ends.

Hitting a ship.

![hit ship](https://user-images.githubusercontent.com/107180641/202029338-bf6d9cb9-a0b0-444e-8089-41d79a94c88f.png)

Selecting same wrong guess again.

![already missed](https://user-images.githubusercontent.com/107180641/202029192-14c2527a-0802-4b07-ba9c-bba5e32650c1.png)

Selecting same hit ship again.

![already hit ship](https://user-images.githubusercontent.com/107180641/202029491-0f84a030-db7b-468b-9350-2a22b3f6b138.png)


#### Game board saves previous coordinates from each round
- All positions that have been chosen on the board get turned to "x" or "-" so in the game function the same coordinates can't be entered multiple times.

#### Printing final board
- This prints board at the end of the game. It shows the location of all the un-hit ships represented with "X" if the user loses the game. If the user wins, the board with show all 5 hit ships represented with "x"

![game over board](https://user-images.githubusercontent.com/107180641/202029863-58b976fa-6e2c-47fe-a28f-a717d88795c5.png)

 
### Future Features
- Allow it to be a 2-player game with the computer randomly guessing coordinates to hit users' ships.


## Data Model

A grid is created that represents the user's board. It holds the 5 randomly generated ships. With each turn, the user's board holds the data of the previous coordinates picked, the location of the ships, and the user's current score and turns left. 
The class "BoardStates" is used which contains enumerations for the different states each position of the board can be: Empty, Alive ships, Hit ships, and Missed guesses.


## Testing

|Features being tested                | How it was manually tested           | Results                     |
|------------------------------------|--------------------------------------|-----------------------------|
|User validation function excepting incorrect input type| Entered nothing, string and floats   | ✓ User asked to enter an integer|
|User validation function excepting number in the board size range | Entering negative integers and integers > 5 | ✓ Message printed to tell the user they cannot enter negative values or numbers bigger than the board size |
| Start game function not decreasing turns left if the same wrong guess coordinate has been selected| Entering the same coordinates for a missed guess| ✓ Message printed telling user they have already guessed that coordinate and to try again|
| Start game function not increasing user score multiple times if the same ship is hit| Entering same coordinates for a known ship location| ✓ Message shows telling user they have already hit this ship and to guess again. User score does not increase and the number of turns left does not decrease| 
|Start game function when the user loses the game| Entering 20 coordinate guesses and not hitting 5 ships | ✓ Results in a message telling the user they have lost the game and they have 0 turns left |
|Start game function when the user wins the game | Entering coordinates and hitting all 5 ships before the turns left = 0 | ✓ Results in a message congratulating the user and telling them they hit all 5 ships and have won the game.| 
| Testing codes format | PEP8 linter / running "pycodestyle" and "pylint" on the run.py file | No error on the run.py file. Only some suggestions on using f-strings and unnecessary use of elif. Pylint rated code 9.67/10 |
| Testing the game format on the Heroku terminal | Deploying battleships game on Heroku terminal | ✓ The game work and can be played on this platform with no errors|

Pylint results.

![pylint results](https://user-images.githubusercontent.com/107180641/202031010-3f96d86c-c41f-4ae5-9117-cbcb148a0d37.png)


### Bugs

#### Resolved Bugs
- Forgot the rows were indexed so kept getting errors that it was out of range, I needed to decrease the range for BOARD_GRID_SIZE to (BOARD_GRID_SIZE -1).
- Selecting the same coordinates kept increasing the user score and decreasing turns left. I added extra if/else-if statements to the state_game function that prompted the user to input a row or column number they haven't picked before if they hit a "-" or "x" on the board.
- The user could select the same ship's coordinates multiple times and the user score would increase. So I fixed his by making the board state different for ships that haven't been hit "X" compared to ships that have been hit "x".

#### Unresolved Bugs
- Label the rows of the grid by spelling "row" vertically next to the row numbers. Tried using "print("%s |%d |%s|" % (i, row_num, row_to_be_printed))" where "i" represented each letter in the string "row" but this just printed the table 6 times. So I have labelled the column but not the row.


### Future Features
Make the game 2-player and add a computer board that allows the computer to guess coordinates on the user board and vice versa.


## Deployment

### Steps for deployment:
1) On Heroku dashboard selected "create new app"
2) Add Buildpacks:
    - python
    - nodejs
3) Add Config Vars:
    - KEY: PORT
    - VALUE: 8000
4) Linked the Heruko app to the GitHub repository "Battleship-Game"
5) Clicked on "Manually Deploy"

Link to live version of this project on the Heroku app: 
https://battleship-game-db.herokuapp.com/

### Steps for cloning branch:
1) On GitHub, on the top right click "Code"
2) Click "local" tab
3) Copy the URL
4) Where you want to clone the file, use command "git clone" and pass through the URL
5) Complete code should now be available on your local system for you to edit 


## Credits
- For helping make the grid layout for the USER_BOARD
    - https://www.youtube.com/watch?v=7Ki_2gr0rsE&ab_channel=DylanIsrael 
- For help with the initial template used to make sure user input was valid.
    - Love Sandwiches module from Code Institute 	
- To label the column and number of rows of the grid. Also for the idea to use a while loop when randomly generating ship coordinates to not get any repeats. The idea for the general if/else-if/else loop that is used in the game function.
    - https://www.youtube.com/watch?v=tF1WRCrd_HQ&ab_channel=KnowledgeMavens - 
- For ideas about adding constants for grid size and the number of ships. Also for the idea of enumerations for the different board states.
    - Mentor Sandeep Aggarwal
- For converting input into integers.
    - https://pynative.com/python-check-user-input-is-number-or-string/#:~:text=To%20check%20if%20the%20input%20string%20is%20an%20integer%20number,using%20the%20int()%20constructor.&text=To%20check%20if%20the%20input%20is%20a%20float%20number%2C%20convert,using%20the%20float()%20constructor.
