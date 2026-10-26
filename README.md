# Tic-Tac-Toe: Player vs. Computer (Python Tkinter)

An interactive graphical Tic-Tac-Toe game created with Python and Tkinter for design and programming evaluation.

---

## 🎮 Overview

This project implements a complete, modern graphical user interface (GUI) for the classic game of Tic-Tac-Toe, featuring a smart Computer AI opponent.

### Key Features
- **User Interface**: Clean, minimalist design with custom color accents and feedback states built using Tkinter.
- **Symbol Selection**: Players can choose to play as **X**, play as **O**, or select **🎲 Random** to let the system assign symbols.
- **First Turn Rule**: In accordance with traditional Tic-Tac-Toe rules, **X always takes the first turn**. If the computer is assigned **X**, it automatically initiates the match.
- **Intelligent Computer AI**:
  1. **Immediate Win**: Scans for any move that completes three-in-a-row for itself.
  2. **Block Opponent**: Blocks the player if they are one step away from winning.
  3. **Strategic Positioning**: Takes the strategic center square (position 4) when available.
  4. **Corner / Edge Strategy**: Chooses corners followed by open edges.
- **Game State Management**:
  - Highlights the winning three-cell line upon victory.
  - Detects draw/tie matches when all 9 grid spaces are filled.
  - Interactive alerts and status bar messages updating each turn.
  - One-click **🔄 Restart Game** button to reset the board.

---

## 💻 Requirements

- **Python 3.8+**
- Standard Python Libraries only:
  - `tkinter` (bundled with standard Python for Windows and macOS)
  - `random`
- **Zero external dependencies** (no `pip install` required).

---

## 🚀 How to Run the Project

### Option 1: Run directly from the root directory (Recommended)

1. Open your terminal / command prompt in this project folder.
2. Run:
   ```bash
   python main.py
   ```
   *On Windows with the Python Launcher:*
   ```cmd
   py main.py
   ```

### Option 2: Run from the `Tic-Tac-Toe` subfolder

```bash
cd Tic-Tac-Toe
python main.py
```

### Option 3: Double-click on Windows
Double-click `main.py` directly from File Explorer.

---

## 📁 Project Structure

```text
├── main.py                     # Primary root entrypoint for easy evaluation
├── README.md                   # Project documentation and evaluation guide
├── .gitignore                  # Git ignore rules for bytecode & cache files
└── Tic-Tac-Toe/
    ├── main.py                 # Game application inside module directory
    └── game.py                 # Game script
```

---

## 📝 Evaluation Notes

- **Entry Point**: You can run `main.py` directly from the root folder.
- **Platform Compatibility**: Tested and fully compatible with Windows, macOS, and Linux.
- **GUI Responsiveness**: Utilizes Tkinter non-blocking event scheduling (`root.after`) for computer AI turns to give realistic pacing and prevent GUI freezing.