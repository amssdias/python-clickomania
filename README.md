# Clickomania

In the game of clickomania, you have to click on the group of boxes having the same colors.

The goal is to remove as many boxes as possible and you will win when all the boxes are removed.

## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up


## Run

- Download the project, open terminal window on folder with "clickomania.py" and type:

```
python clickomania.py
```

## Files


### Clickomania.py

This is the file we will run, we only have a module to import and to call the main function to create the game

### Layout.py

In this file I have created all the global variables plus the layout of the game. 

### Commands.py

In here I have builted the two main functions `create_game` to create the game, even when we click on the reset button, and `activate` to activate the color of the button and check if two squares are equal.