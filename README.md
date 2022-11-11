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



BATTLESHIP GAME
reason for game
purpose it serves 
target audience...

[screenshot of it on different devices]


Rules of game...
key of what dif symbols mean...

Features...
- personalised board printed with user name...
- board labelled with x and y axis
- 5 random coordinates generated 
- user guesses inputs... input need to be valid if not they are asked to insert input again...
- game function for if coordinate miss "-".
- if coordinate hit "X"
- if coordinate already "X" of "-" they need to input again
- if coordinate not entered user needs to input again
- if not turns left OR score ==5 game over.


data model...

TESTING
PEP8 linter
checked invalid inputs can be entered and does exit game
test game outputs of heroku terminal... i.e game stops if no turns left or 5 is scored.


bugs...
resolves bugs...
- forgetted the rows were indexed so kept getting errors that it was out of range i just needed to decrease range for 0-6 to 0-5.


deployment...


credits...



unresolved bugs...

future features...
allow random coordinates on user board and computer to guess and try to hit users board... add to game function "while computer_score <5.."
