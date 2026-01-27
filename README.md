# Blackjack-waterfall
A simple implementation of blackjack using pygame using the waterfall metholodgy.

__[Requires Python 3.13 or older and Pygame installed]__

# Installation & Setup

Install Python from here: https://www.python.org/downloads/release/python-31311/

Install Pygame using this command:
```
pip install pygame tomllib
```

Extract the .zip file and run main.py by double clicking it and selecting python.

# GamePlay

It's you VS the Dealer!
Your goal is to have a higher total than the dealer without going over 21. Press the "Hit" button to draw a new card and add it to your total. Press the "Stand" Button to end your turn without drawing a new card. If you go over 21, You bust and lose the game. If anyone reaches exactly 21, it's Blackjack and the person with 21 wins instantly. When you and the dealer have hands matching in value, it's called a push and the game is declared a draw. If you have 2 cards of the same value, you can choose to play them as seperate hands, this is called a split. After the game ends, you can press the "R" key to try again or press the "Q" key to exit the game.
