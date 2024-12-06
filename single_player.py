import tkinter as tk
from tkinter import messagebox
from utils import check_winner, is_draw, reset_board
from ai_logic import easy_move, medium_move, impossible_move
import sys
import subprocess

def single_player_game(mode):
    root = tk.Tk()
    root.title(f"Tic-Tac-Toe ({mode.capitalize()} Mode)")
    root.geometry("500x500")  # Modern initial size

    # Configure grid weights for resizing
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(3, weight=1)

    # Initialize game board and current player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = ["X"]
    game_locked = [False]  # Lock mechanism to prevent extra moves

    def reset_game():
        """Reset the game for a new round."""
        nonlocal board, current_player
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player[0] = "X"
        game_locked[0] = False
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(text=" ", state="normal")  # Reset buttons

    def end_game(message):
        """Handle end-of-game actions."""
        choice = messagebox.askyesno("Game Over", f"{message}\n\nDo you want to play again?")
        if choice:
            reset_game()
        else:
            root.destroy()  # Close the game window
            subprocess.run([sys.executable, "main_menu.py"])  # Return to the main menu

    def make_move(row, col):
        if board[row][col] == " " and not game_locked[0]:
            board[row][col] = current_player[0]
            buttons[row][col].config(text=current_player[0], state="disabled", fg="black")  # Set text color to black
            if check_winner(board, current_player[0]):
                end_game(f"Player {current_player[0]} wins!")
            elif is_draw(board):
                end_game("It's a draw!")
            else:
                current_player[0] = "O"
                game_locked[0] = True  # Lock the game during AI move
                root.after(500, ai_move)  # Add a small delay for AI move

    def ai_move():
        if mode == "easy":
            row, col = easy_move(board)
        elif mode == "medium":
            row, col = medium_move(board, "O", "X")
        elif mode == "impossible":
            row, col = impossible_move(board, "O", "X")
        board[row][col] = "O"
        buttons[row][col].config(text="O", state="disabled", fg="black")  # Set text color to black
        if check_winner(board, "O"):
            end_game("AI wins!")
        elif is_draw(board):
            end_game("It's a draw!")
        else:
            current_player[0] = "X"
        game_locked[0] = False  # Unlock the game after AI move

    def pause_game():
        # Pause dialog
        choice = messagebox.askyesno("Pause Menu", "Do you want to go back to the main menu?")
        if choice:
            root.destroy()  # Close the current game window
            subprocess.run([sys.executable, "main_menu.py"])

    # Create the game board buttons
    buttons = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(root, text=" ", font=("Helvetica", 20),
                                          command=lambda r=row, c=col: make_move(r, c))
            buttons[row][col].grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    # Add a modern pause button
    pause_button = tk.Button(root, text="Pause", font=("Helvetica", 20), command=pause_game)
    pause_button.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)

    root.configure(background="#f0f0f0")  # Light gray background
    root.mainloop()
