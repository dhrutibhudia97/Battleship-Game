![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome dhrutibhudia97,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.


-----
Happy coding!



# BATTLESHIP GAME

The BattleShip game is a game in the python terminal run using Heroku.
The aim of this game is for users to try and find the computers 5 battleships on the game board by guessing the coordinates correctly in 20 turns or under. 
The board grid size is (6x6), has 36 spaces and each of the 5battleships takes up 1 space.
This game can entertain the user with minimal knowledge needed before hand so it is easy for anyone to play, as no other player is needed and they just need to guess a row and colun number.

[insert screenshot of it on different devices.]


## The Rules Of The Game

Battleships game is based of the 2 player board game when users take it in turn to guess where the ship is on there users board and it they guess correctly they destroy the ship. More info about this game can be found here: https://en.wikipedia.org/wiki/Battleship_(game)

This game varies slightly by firstly being 1 player so the user is just guessing where the computers ships are.
The different symbols of the board represent the different states the locations on the board can be in.

- Initially the board is printed, all positions are represented with "o" with represents and empty space that can be hit.
- Once the users guess a valid row and column number, this coordinate on the board is checked to see if that position is empty in which case the "o" turns to "-" representing a wrong guess. 
- If the location they hit has a ship the "o" turns to a "x" that represents a ship has been hit.
- To win this game the user need to hit all 5 computer ships and get 5 "x" on their board before their 20 turns are finished.


## Features

### Existing Feature

#### Random Coordinate Generator
- Computer generates 5 random coordinates to place ships on game board using the random library thats been imported.
- User cannot see where the ships have been places as the symbols for the ships have been replaced with the symbol for empty before the the board is printed.
[insert screenshot of board before input given]

#### The User Input Validator 
- The row and column number input is checked to see if any data has been inputted, then checking to see if it is an integer. If it isn't an integer than user asked to input row or column number again.
- If it is an integer is is checked to see if it is a positive number and if it is smaller then the board grid size. If it isn't the user as asked to input the row or column number again.
[insert screenshot of entering nothing/float/string/negative integer and too big an integer]

#### The Game Function Validator
- User inserts name which will be printed on top of the game board for each round.
- The same coordinates cannot be entered again. If it has, turns left and user score don't change. User is told they have already hit this location and asked to insert another value.
- If coordinate hasn't been entered before, coordinate checked to see if it hits or misses a ship, deducting 1 from turns left and adding 1 to user score accordingly.
- The game function stops running when either the turns left is 0 or the user score is 5. The last game is printed and game ends.
[insert screenshot or a hit]
[miss ship ]
[already hit ship]
[already missed location.]
[insert screenshot of either hitting all ships and winning the game]
[losing game by not hitting all ships.]

#### The User Coordinates Are Saved For Each Round Of The Game.
 

### Future Features
- Allow it to be a 2 player game with computer randomly guessing coordinates to hit users ships.
- Allow various battleship sizes to take up more than one coordinate space.


## Data Model

A grid is created that represents the users board. It holds the 5 randomly generated ships. When each turn the users board hold the data of the previous coordinates picked. The location of the ships and the users current score and turns left. 
The class "BoardStates" is used which contain enumerations for the different states each position of the board can be: Empty, Alive ships, Hit ships and Missed guesses.


## Testing
- I have manually checked that the users inputs are valid before the game function runs. When the users row or column input is: blank, a string, float, a negative integer or a integer bigger than 5 the user is prompted to enter another input.
- I have tested that the users inputs in the game function effects the users score and turns left correctly. If the same coordinate is selected this has no effect on the turns left or user score.

- Test game outputs of heroku terminal... i.e game stops if no turns left or 5 is scored...
- - PEP8 linter


### Bugs

#### Resolved Bugs
- Forgot the rows were indexed so kept getting errors that it was out of range, I needed to decrease range for BOARD_GRID_SIZE to (BOARD_GRID_SIZE -1).
- Selecting the same coordinates kept increasing the user score and decreasing turns left. I added extra if/elif statements to the state_game function that prompted user to input row or column number they haven't picked before if they hit a "-" or "x" on the board.

#### Unresolved Bugs
- No unresolved bugs.


### Future Features
Make game 2 player and add a computer board which allows computer to guess coordinates on user board and vice versa.


## Deployment


## Credits
- https://www.youtube.com/watch?v=7Ki_2gr0rsE&ab_channel=DylanIsrael - for making board and layout of grid.
- love sandwiches module used for template for user input and making sure its valid.		
- https://www.youtube.com/watch?v=tF1WRCrd_HQ&ab_channel=KnowledgeMavens - labeling column of user and computer grid using print("%d|%s"..)








