## Requirements
This terminal-based Blackjack game is written in Python 3. The only required library is `random`, which comes with the Python standard library, so no additional installation is needed. To begin playing, simply execute `python3 blackjack.py`.

## Gameplay
The game implements the standard rules of Blackjack. Any expected inputs are indicated by in-game prompts. Currently, the game tallies totals the number of rounds won by the player and (electronic) dealer to determine a winner. Gameplay ends when there are no more cards to be dealt; the player has the option of specifying how many standard decks to play with.

## Design
Python's `random` library is used to simulate the shuffling of cards. The calculation of card and hand values is partitioned into functions to keep the calculations for "soft hands" (the dual value of Aces) clean. The string display formatting of cards is also partitioned into functions so as to keep the separation between verbosity modes (i.e. "JH" vs. "Jack of Hearts", decided by the user) clean.

## Features for the future
I haven't had much time to work on the current version of the game, but with more time, I would like to incorporate (in rough order of priority):
- Placement of monetary bets
- "Splitting pairs" and "doubling down", additional options in a blackjack game
- Modification of the game's terminal outpu, to make it aesthetically more streamlined for the player (perhaps using carriage returns or real-time delays in between player and dealer turns)
- A multiplayer option

### Have fun playing!
