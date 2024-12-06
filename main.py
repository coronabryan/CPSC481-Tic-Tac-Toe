# Tic-Tac-Toe Game

# Initialize the board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Display the board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if a player has won
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full (draw)
def is_draw(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

# Main game function
def play_game():
    board = create_board()
    players = ["X", "O"]
    turn = 0
    
    while True:
        display_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn!")
        
        # Get user input
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers between 0 and 2 separated by a space.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Check for a win or draw
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch turn
        turn += 1

# Run the game
play_game()
