import copy
import math

# Constants for the game
X = "X"  # Player X
O = "O"  # Player O
EMPTY = None  # Empty cell

# Function to determine the next player based on the board state
def player(board):
    # Count X's and O's on the board to decide the next player
    Xs = sum(row.count(X) for row in board)
    Os = sum(row.count(O) for row in board)
    return X if Xs <= Os else O  # X goes first

# Function to find all available actions (empty cells) on the board
def actions(board):
    return {(y, x) for y in range(3) for x in range(3) if board[y][x] == EMPTY}

# Function to return the board state resulting from a move
def result(board, action):
    if len(action) != 2:
        raise Exception("Invalid action")
    y, x = action
    if board[y][x] != EMPTY:
        raise Exception("Invalid move: cell is already occupied")
    board_copy = copy.deepcopy(board)
    board_copy[y][x] = player(board)
    return board_copy

# Function to determine if there is a winner
def winner(board):
    for y in range(3):
        if board[y][0] == board[y][1] == board[y][2] and board[y][0] is not None:
            return board[y][0]
        if board[0][y] == board[1][y] == board[2][y] and board[0][y] is not None:
            return board[0][y]
    if (board[0][0] == board[1][1] == board[2][2] or
        board[0][2] == board[1][1] == board[2][0]) and board[1][1] is not None:
        return board[1][1]
    return None

# Function to check if the game has ended
def terminal(board):
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)

# Function to return the utility value of the board
def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

# Minimax function to determine the best move
def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:  # Maximizing for X
        _, best_action = maxvalue(board)
    else:  # Minimizing for O
        _, best_action = minvalue(board)

    return best_action

# Min value function for minimax algorithm
def minvalue(board):
    if terminal(board):
        return utility(board), None

    min_score = math.inf
    best_action = None
    for action in actions(board):
        score, _ = maxvalue(result(board, action))
        if score < min_score:
            min_score = score
            best_action = action
    return min_score, best_action

# Max value function for minimax algorithm
def maxvalue(board):
    if terminal(board):
        return utility(board), None

    max_score = -math.inf
    best_action = None
    for action in actions(board):
        score, _ = minvalue(result(board, action))
        if score > max_score:
            max_score = score
            best_action = action
    return max_score, best_action

# Function to print the board in a readable format
def print_board(board):
    for row in board:
        print(" | ".join([cell if cell else " " for cell in row]))
        print("-" * 9)

# Main game loop function
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    while not terminal(board):
        print_board(board)

        if player(board) == X:  # Player X's turn
            try:
                row, col = map(int, input("Enter your move (row col): ").split())
                action = (row, col)
                board = result(board, action)
            except Exception as e:
                print(f"Invalid move: {e}")
        else:  # Player O's turn (minimax algorithm)
            print("Computer is making a move...")
            action = minimax(board)
            board = result(board, action)

    print_board(board)
    winner_player = winner(board)
    if winner_player:
        print(f"{winner_player} wins!")
    else:
        print("It's a tie!")

# Start the game
if __name__ == "__main__":
    play_game()