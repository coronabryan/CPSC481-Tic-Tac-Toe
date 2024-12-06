import random
from utils import check_winner

def easy_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def medium_move(board, player, opponent):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    board[row][col] = " "
                    return (row, col)
                board[row][col] = " "

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = opponent
                if check_winner(board, opponent):
                    board[row][col] = " "
                    return (row, col)
                board[row][col] = " "

    return easy_move(board)

def impossible_move(board, player, opponent):
    def minimax(board, is_maximizing):
        if check_winner(board, player):
            return 1
        if check_winner(board, opponent):
            return -1
        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = player
                        score = minimax(board, False)
                        board[row][col] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = opponent
                        score = minimax(board, True)
                        board[row][col] = " "
                        best_score = min(best_score, score)
            return best_score

    best_score = -float('inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                score = minimax(board, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move
