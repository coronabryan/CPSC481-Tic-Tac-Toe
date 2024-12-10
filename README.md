
# Tic-Tac-Toe Game with GUI and AI

## **Overview**
This project is a Python-based implementation of Tic-Tac-Toe, featuring a graphical user interface (GUI) built with `tkinter`. It includes two game modes:
- **Single-Player Mode:** Play against an AI with three difficulty levels: Easy, Medium, and Impossible.
- **Two-Player Mode:** Play locally against another player on the same device.

The project is structured into multiple files to separate concerns and improve readability, making it easier to understand and maintain.

---

## **Layout of the Code**
The project directory is organized as follows:

```
TicTacToe/
├── main_menu.py
├── two_player.py
├── single_player.py
├── ai_logic.py
├── utils.py
└── README.md
```

### **Files and Their Purposes**

#### 1. `main_menu.py`
- **Purpose:** 
  - Acts as the entry point for the game.
  - Provides a main menu interface where players can select between game modes: 2-Player, Easy, Medium, and Impossible.
  - Handles transitions to the selected game mode.
- **Key Features:**
  - GUI layout for the main menu.
  - Buttons to navigate to specific game modes.
- **How it works:** 
  - When a button is clicked, the corresponding game mode (from `two_player.py` or `single_player.py`) is launched.

---

#### 2. `two_player.py`
- **Purpose:** 
  - Implements the two-player mode, allowing two players to take alternate turns on the same device.
- **Key Features:**
  - A game board represented as a 3x3 grid of buttons.
  - Tracks player turns (X and O).
  - Detects win and draw conditions.
  - Includes a reset option to play multiple rounds seamlessly.
- **How it works:**
  - Each button corresponds to a cell on the board. Clicking a button marks it for the current player and checks for win/draw conditions.
  - If a player wins or the game ends in a draw, it prompts the players to restart or return to the main menu.

---

#### 3. `single_player.py`
- **Purpose:** 
  - Implements the single-player mode with AI opponents of varying difficulty levels (Easy, Medium, Impossible).
- **Key Features:**
  - A game board represented as a 3x3 grid of buttons.
  - AI decision-making logic integrated for different difficulty levels.
  - Detects win and draw conditions.
  - Includes a reset option to play multiple rounds seamlessly.
- **How it works:**
  - The player makes a move by clicking a button, and the AI responds based on the selected difficulty:
    - **Easy Mode:** AI moves randomly.
    - **Medium Mode:** AI uses basic heuristics to block the player or win.
    - **Impossible Mode:** AI uses the minimax algorithm to make optimal moves.
  - Game state is continuously updated until a win or draw occurs.

---

#### 4. `ai_logic.py`
- **Purpose:** 
  - Contains the logic for AI decision-making in single-player mode.
- **Key Features:**
  - **Easy Mode:** Generates random moves.
  - **Medium Mode:** Implements simple heuristics to prioritize winning or blocking.
  - **Impossible Mode:** Uses the **minimax algorithm** to evaluate all possible outcomes and choose the best move.
- **How it works:**
  - Exposes functions (`easy_move`, `medium_move`, `impossible_move`) called by `single_player.py` during gameplay.

---

#### 5. `utils.py`
- **Purpose:** 
  - Contains shared utility functions for managing game logic.
- **Key Features:**
  - **Win Detection:** Checks rows, columns, and diagonals for a winning pattern.
  - **Draw Detection:** Checks if the board is full with no winners.
  - **Reset Functionality:** Resets the game board and button states for a new round.
- **How it works:**
  - Functions are imported and used in both `single_player.py` and `two_player.py` to keep logic centralized and reusable.

---

## **How to Run the Project**
1. **Prerequisites:**
   - Python 3.6 or higher installed on your system.
   - No additional dependencies are required (uses built-in Python libraries).

2. **Steps:**
   - Clone or download the project.
   - Navigate to the project directory.
   - Run the `main_menu.py` file to start the game:
     ```bash
     python main_menu.py
     ```
   - Select a game mode from the main menu.

---

## **How the Code Works**
1. **Main Menu:**  
   - Launches and provides navigation options for 2-player or single-player modes with difficulty levels.

2. **Gameplay:**
   - The game board is displayed as a 3x3 grid of buttons.
   - Each button click triggers an event to mark the board and update the game state.
   - Single-player mode uses `ai_logic.py` to generate AI responses.

3. **Game Flow:**
   - Players alternate moves.
   - The system checks for a win or draw after each move.
   - Prompts the user to restart or quit after the game ends.

4. **AI Functionality:**
   - Easy Mode: AI selects a random empty cell.
   - Medium Mode: AI tries to win or block the player.
   - Impossible Mode: AI uses the minimax algorithm to always make the optimal move.

---

## **Key Features**
- Fully functional GUI for gameplay.
- Intelligent AI for single-player mode.
- Seamless replay functionality with game state resetting.
- Responsive layout that adjusts to resizing.

---

