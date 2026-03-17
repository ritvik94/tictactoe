# Tic-Tac-Toe AI (Minimax)

A terminal-based implementation of Tic-Tac-Toe where a human player competes against an unbeatable AI. The AI utilizes the **Minimax Algorithm** to ensure it never loses, always playing for a win or a forced draw.

---

##  Features
* **Unbeatable AI**: The computer evaluates every possible game outcome to choose the optimal move.
* **Recursive Decision Making**: Implements `maxvalue` and `minvalue` functions to simulate opponent responses.
* **Clean Interface**: Simple coordinate-based input and an ASCII-rendered game board.
* **Deep Copy Logic**: Uses the `copy` module to simulate future board states without affecting the current game.

---

##  How It Works: The Minimax Algorithm
The core of this project is the **Minimax** algorithm, a recursive strategy used in two-player, zero-sum games.

1.  **Maximizing Player (X)**: Tries to choose a move that results in the highest possible score.
2.  **Minimizing Player (O)**: Tries to choose a move that results in the lowest possible score.
3.  **Terminal States**: At the end of a game branch, the AI assigns a utility value:
    * **+1**: Player X wins.
    * **-1**: Player O wins.
    * **0**: The game is a tie.

[Image of Minimax algorithm tree for Tic-Tac-Toe]

---

##  How to Play
1.  **Ensure Python is installed**: You will need Python 3.x.
2.  **Run the script**:
    ```bash
    python tictactoe.py
    ```
3.  **Enter your move**: When prompted `Enter your move (row col):`, type the row
