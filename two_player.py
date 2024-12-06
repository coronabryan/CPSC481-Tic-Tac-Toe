import tkinter as tk
from tkinter import messagebox
from utils import check_winner, is_draw, reset_board
import sys
import subprocess

def two_player_game():
    root = tk.Tk()
    root.title("Tic-Tac-Toe (2-Player)")
    root.geometry("500x500")  # Modern initial size

    # Configure grid weights for resizing
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(3, weight=1)

    # Initialize game board and current player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = ["X"]

    def reset_game():
        """Reset the game for a new round."""
        nonlocal board, current_player
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player[0] = "X"
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
        if board[row][col] == " ":
            board[row][col] = current_player[0]
            buttons[row][col].config(text=current_player[0], state="disabled", fg="black")  # Set text color to black
            if check_winner(board, current_player[0]):
                end_game(f"Player {current_player[0]} wins!")
            elif is_draw(board):
                end_game("It's a draw!")
            else:
                current_player[0] = "O" if current_player[0] == "X" else "X"

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
