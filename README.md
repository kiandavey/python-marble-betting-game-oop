# 💎 Marble Betting Game (OOP Console Application)

This project is a single-player, command-line simulation of a marble betting game built using **Object-Oriented Programming (OOP)** principles in Python. The game separates the player's state and actions (`Player` class) from the game environment and mechanics (`MarbleGame` class) to create a clean, maintainable structure.

The simulation runs until the specified number of rounds is completed or the player loses half of their starting gold.

---

## 🕹️ Game Rules and Features

### Core Mechanics
* **Starting Gold:** The player begins with a fixed amount of **Gold Pieces** (1000 in the default configuration).
* **Game Over Condition:** The game ends immediately if the player's gold balance drops to **half or less** of their starting amount.
* **Interactive Input:** The player is prompted for the number of rounds and their bet amount before each round.
* **Robustness:** The code includes extensive **`try...except`** blocks and validation logic to prevent crashes from non-numeric or invalid bet inputs (e.g., betting more than current gold).

### Marble Bag Composition (Total 10 Marbles)
Marbles are replaced after every draw, keeping the odds constant throughout the game.

| Marble Color | Count | Odds | Payout/Loss | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Green** | 5 | 50% | **+1x** Bet | Standard Win |
| **Red** | 3 | 30% | **-1x** Bet | Standard Loss |
| **Black (10X)** | 1 | 10% | **+10x** Bet | **Jackpot** Win |
| **White (5X)** | 1 | 10% | **-5x** Bet | High-Risk Loss |

---

## 🚀 How to Run the Game

### Prerequisites
You need **Python 3** installed on your system.

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd [your-repo-name]
    ```
3.  **Run the Script:**
    ```bash
    python your_script_name.py
    ```
    *(Note: Replace `your_script_name.py` with the actual name of your Python file.)*

---

## ⚙️ Project Structure (OOP)

The game's logic is cleanly divided between two classes, demonstrating strong separation of concerns:

### 1. `Player` Class
* **Responsibility:** Manages the player's state (gold, name, win/loss stats).
* **Key Methods:**
    * `make_bet()`: Validates that the player can afford the bet.
    * `round_count()`: Handles robust input for the total number of rounds.

### 2. `MarbleGame` Class
* **Responsibility:** Manages the game environment and mechanics.
* **Key Method:**
    * `run_round()`: Controls the main game loop, handles marble drawing, determines payouts, updates the `Player` object's gold, and checks for the Game Over condition.
