import tkinter as tk
from tkinter import ttk
from game_manager import start_game

def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("500x500")  # Set a larger initial size for the modern look

    # Apply a modern theme and style
    style = ttk.Style()
    style.theme_use("clam")  # Use a clean, modern theme
    style.configure("TButton", font=("Helvetica", 16), padding=10)
    style.configure("TLabel", font=("Helvetica", 24, "bold"), anchor="center")
    style.configure("Title.TLabel", foreground="#333", background="#f0f0f0", padding=20)

    # Configure row and column weights for resizing
    root.grid_rowconfigure(0, weight=1)  # Title row
    for i in range(1, 5):  # Button rows
        root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create the title label
    title_label = ttk.Label(root, text="Welcome to Tic-Tac-Toe", style="Title.TLabel")
    title_label.grid(row=0, column=0, sticky="nsew")

    # Create buttons for game modes
    ttk.Button(root, text="2-Player Mode", command=lambda: handle_mode_selection(root, "2-player")).grid(
        row=1, column=0, sticky="nsew", padx=20, pady=10
    )
    ttk.Button(root, text="Easy Mode", command=lambda: handle_mode_selection(root, "easy")).grid(
        row=2, column=0, sticky="nsew", padx=20, pady=10
    )
    ttk.Button(root, text="Medium Mode", command=lambda: handle_mode_selection(root, "medium")).grid(
        row=3, column=0, sticky="nsew", padx=20, pady=10
    )
    ttk.Button(root, text="Impossible Mode", command=lambda: handle_mode_selection(root, "impossible")).grid(
        row=4, column=0, sticky="nsew", padx=20, pady=10
    )

    root.configure(background="#f0f0f0")  # Light gray background
    root.mainloop()

def handle_mode_selection(root, mode):
    root.destroy()  # Close the main menu
    start_game(mode)  # Start the selected game mode

if __name__ == "__main__":
    main_menu()
