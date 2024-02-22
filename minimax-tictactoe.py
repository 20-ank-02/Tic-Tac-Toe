import math
import random

"""
This module implements a Tic Tac Toe game with an AI opponent using the Minimax algorithm with easy, medium, hard difficulties.

Functions:
    - print_board(board): Prints the Tic Tac Toe board.
    - check_win(board, player): Checks if a player has won.
    - check_draw(board): Checks if the board is full (draw).
    - possible_moves(board): Generates all possible moves on the board.
    - minimax(board, depth, max_depth, is_maximizing): The Minimax algorithm implementation.
    - find_best_move(board, max_depth): Finds the best move using the Minimax algorithm.
    - play_game(): Function to play the Tic Tac Toe game.
"""

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(col == player for col in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to generate all possible moves
def possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Minimax function
def minimax(board, depth, max_depth,is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif check_draw(board):
        return 0
    elif depth == max_depth:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in possible_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1,max_depth, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in possible_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1,max_depth, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

# Function to find the best move using the minimax algorithm
def find_best_move(board,max_depth):
    best_score = -math.inf
    best_move = None
    for move in possible_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, max_depth,False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Function to play the game
def play_game():
    board = [[' ']*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    difficulty=input("Select difficulty (easy,medium,hard): ")
    if difficulty=='medium':
        max_depth=2
    elif difficulty=='hard':
        max_depth=math.inf
    elif difficulty=='easy':
        max_depth=0
    print_board(board)

    while True:
        player_row = int(input("Enter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))

        if board[player_row][player_col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[player_row][player_col] = 'X'

        if check_win(board, 'X'):
            print("Player X wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        if max_depth:
            ai_row, ai_col = find_best_move(board,max_depth)
        else:
            ai_row, ai_col = random.choice(possible_moves(board))
        board[ai_row][ai_col] = 'O'

        print_board(board)

        if check_win(board, 'O'):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
