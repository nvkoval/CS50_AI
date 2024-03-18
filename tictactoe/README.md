## [Tic-Tac-Toe](https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/)

Using Minimax, implement an AI to play Tic-Tac-Toe optimally.

### Specification

Complete the implementations of `player`, `actions`, `result`, `winner`, `terminal`, `utility`, and `minimax`.

- The `player` function should take a `board` state as input, and return which player’s turn it is (either `X` or `O`).
- The `actions` function should return a `set` of all of the possible actions that can be taken on a given board.
- The `result` function takes a `board` and an `action` as input, and should return a new board state, without modifying the original board.
- The `winner` function should `accept` a board as input, and return the winner of the board if there is one.
- The `terminal` function should accept a `board` as input, and return a boolean value indicating whether the game is over.
- The `utility` function should accept a terminal `board` as input and output the utility of the board.
- The `minimax` function should take a `board` as input, and return the optimal move for the player to move on that board.

For all functions that accept a `board` as input, you may assume that it is a valid board (namely, that it is a list that contains three rows, each with three values of either `X`, `O`, or `EMPTY`). You should not modify the function declarations (the order or number of arguments to each function) provided.
