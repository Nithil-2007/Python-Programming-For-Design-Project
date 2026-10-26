"""
Tic-Tac-Toe: Player vs. Computer (Tkinter GUI)
-----------------------------------------------
A graphical Tic-Tac-Toe game created with Python and Tkinter.
Features:
- Play as X, O, or let the game choose randomly.
- Smart AI computer opponent with blocking and winning strategies.
- Visual highlight for winning combination and clean modern interface.

How to Run:
    python game.py   (or: py game.py)
"""

import tkinter as tk
from tkinter import messagebox
import random

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe: Player vs Computer")
root.geometry("380x540")
root.resizable(False, False)
root.configure(bg="#F7F9FC")

# Game variables
player_symbol = None    # "X" or "O"
computer_symbol = None  # "O" or "X"
current_turn = None     # "X" or "O" (X always starts)
game_over = False
game_started = False
buttons = []

# Winning combinations
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# Check if someone has won
def check_winner():
    for a, b, c in wins:
        if (buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != ""):
            return buttons[a]["text"], (a, b, c)
    return None, None

# Helper to check if a specific move wins for a given symbol
def will_win(index, symbol):
    for a, b, c in wins:
        if index in (a, b, c):
            cells = [buttons[pos]["text"] if pos != index else symbol for pos in (a, b, c)]
            if cells[0] == cells[1] == cells[2] == symbol:
                return True
    return False

# Computer AI Turn
def computer_turn():
    global current_turn, game_over

    if game_over or not game_started or current_turn != computer_symbol:
        return

    empty_indices = [i for i, b in enumerate(buttons) if b["text"] == ""]
    if not empty_indices:
        return

    chosen_move = None

    # 1. Winning move: If computer can win immediately, take it
    for move in empty_indices:
        if will_win(move, computer_symbol):
            chosen_move = move
            break

    # 2. Blocking move: If player is about to win, block them
    if chosen_move is None:
        for move in empty_indices:
            if will_win(move, player_symbol):
                chosen_move = move
                break

    # 3. Center square (best strategic move)
    if chosen_move is None and 4 in empty_indices:
        chosen_move = 4

    # 4. Corner squares
    if chosen_move is None:
        corners = [i for i in [0, 2, 6, 8] if i in empty_indices]
        if corners:
            chosen_move = random.choice(corners)

    # 5. Side squares
    if chosen_move is None:
        chosen_move = random.choice(empty_indices)

    # Place computer's symbol
    fg_color = "#1565C0" if computer_symbol == "X" else "#C62828"
    buttons[chosen_move].config(text=computer_symbol, fg=fg_color)

    winner, combo = check_winner()
    if winner:
        game_over = True
        for idx in combo:
            buttons[idx].config(bg="#FFCDD2")
        status.config(text="Game Over: Computer Wins! 🤖", fg="#C62828")
        messagebox.showinfo("Game Over", "Computer Wins! 🤖 Better luck next time!")
    elif all(b["text"] != "" for b in buttons):
        game_over = True
        status.config(text="Game Over: It's a Draw! 🤝", fg="#455A64")
        messagebox.showinfo("Game Over", "It's a Draw! 🤝")
    else:
        current_turn = player_symbol
        status.config(text=f"Your Turn ({player_symbol})", fg="#2E7D32")

# Player click function
def click(index):
    global current_turn, game_over

    if not game_started:
        status.config(text="⚠️ Please choose X, O, or 🎲 Random first!", fg="#E65100")
        return

    if game_over or current_turn != player_symbol:
        return

    if buttons[index]["text"] == "":
        fg_color = "#1565C0" if player_symbol == "X" else "#C62828"
        buttons[index].config(text=player_symbol, fg=fg_color)

        winner, combo = check_winner()
        if winner:
            game_over = True
            for idx in combo:
                buttons[idx].config(bg="#C8E6C9")
            status.config(text="Game Over: You Win! 🎉", fg="#2E7D32")
            messagebox.showinfo("Game Over", "Congratulations! You Win! 🎉")
        elif all(b["text"] != "" for b in buttons):
            game_over = True
            status.config(text="Game Over: It's a Draw! 🤝", fg="#455A64")
            messagebox.showinfo("Game Over", "It's a Draw! 🤝")
        else:
            current_turn = computer_symbol
            status.config(text="Computer is thinking... 🤖", fg="#546E7A")
            root.after(450, computer_turn)

# Choose symbol / starter
def choose_symbol(choice):
    global player_symbol, computer_symbol, current_turn, game_started, game_over

    if game_started and any(b["text"] != "" for b in buttons):
        return

    is_random = (choice == "random")
    if is_random:
        player_symbol = random.choice(["X", "O"])
    else:
        player_symbol = choice

    computer_symbol = "O" if player_symbol == "X" else "X"
    current_turn = "X"  # X always takes the first turn
    game_started = True
    game_over = False

    # Disable symbol selection during active game
    btn_x.config(state="disabled", relief="groove")
    btn_o.config(state="disabled", relief="groove")
    btn_random.config(state="disabled", relief="groove")

    # Clear board if restarting
    for b in buttons:
        b.config(text="", bg="#FFFFFF")

    prefix = "🎲 Random Pick: " if is_random else ""
    if player_symbol == "X":
        status.config(text=f"{prefix}You are X! Your Turn", fg="#2E7D32")
    else:
        status.config(text=f"{prefix}You are O! Computer (X) starts...", fg="#546E7A")
        root.after(500, computer_turn)

# Restart game
def restart():
    global current_turn, game_over, game_started, player_symbol, computer_symbol

    game_over = False
    game_started = False
    player_symbol = None
    computer_symbol = None
    current_turn = None

    for button in buttons:
        button.config(text="", bg="#FFFFFF")

    btn_x.config(state="normal", relief="raised")
    btn_o.config(state="normal", relief="raised")
    btn_random.config(state="normal", relief="raised")

    status.config(text="Choose X, O, or 🎲 Random to Start", fg="#37474F")

# Title
title = tk.Label(
    root, text="TIC-TAC-TOE",
    font=("Arial", 20, "bold"),
    bg="#F7F9FC", fg="#263238"
)
title.pack(pady=(12, 2))

subtitle = tk.Label(
    root, text="Player vs Computer",
    font=("Arial", 10, "italic"),
    bg="#F7F9FC", fg="#78909C"
)
subtitle.pack(pady=(0, 8))

# Symbol Selection Frame
choice_frame = tk.LabelFrame(
    root, text=" Choose Your Symbol ",
    font=("Arial", 10, "bold"),
    bg="#F7F9FC", fg="#37474F",
    padx=10, pady=6
)
choice_frame.pack(pady=4)

btn_x = tk.Button(
    choice_frame, text="Play as X",
    font=("Arial", 10, "bold"),
    width=9, bg="#E3F2FD", fg="#1565C0",
    activebackground="#BBDEFB",
    command=lambda: choose_symbol("X")
)
btn_x.grid(row=0, column=0, padx=5)

btn_o = tk.Button(
    choice_frame, text="Play as O",
    font=("Arial", 10, "bold"),
    width=9, bg="#FFEBEE", fg="#C62828",
    activebackground="#FFCDD2",
    command=lambda: choose_symbol("O")
)
btn_o.grid(row=0, column=1, padx=5)

btn_random = tk.Button(
    choice_frame, text="🎲 Random",
    font=("Arial", 10, "bold"),
    width=9, bg="#EDE7F6", fg="#4A148C",
    activebackground="#D1C4E9",
    command=lambda: choose_symbol("random")
)
btn_random.grid(row=0, column=2, padx=5)

# Status label
status = tk.Label(
    root, text="Choose X, O, or 🎲 Random to Start",
    font=("Arial", 12, "bold"),
    bg="#F7F9FC", fg="#37474F"
)
status.pack(pady=8)

# Game board frame
frame = tk.Frame(root, bg="#B0BEC5", padx=3, pady=3)
frame.pack(pady=6)

for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 22, "bold"),
        width=4,
        height=2,
        bg="#FFFFFF",
        relief="ridge",
        bd=2,
        command=lambda i=i: click(i)
    )
    button.grid(row=i // 3, column=i % 3, padx=2, pady=2)
    buttons.append(button)

# Restart button
restart_button = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 12, "bold"),
    bg="#ECEFF1",
    fg="#263238",
    padx=12, pady=4,
    command=restart
)
restart_button.pack(pady=12)

# Run application
if __name__ == "__main__":
    root.mainloop()
