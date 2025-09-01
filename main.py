import tkinter as tk
from tkinter import font

# --- Game state ---
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None]*3 for _ in range(3)]
game_over = False

# --- Helper functions ---
def check_winner():
    # rows & columns
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # diagonals
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # draw?
    if all(board[r][c] != "" for r in range(3) for c in range(3)):
        return "Draw"

    return None

def disable_all():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")

def on_click(r, c):
    global current_player, game_over
    if game_over or board[r][c] != "":
        return

    board[r][c] = current_player
    buttons[r][c].config(text=current_player, state="disabled")

    winner = check_winner()
    if winner:
        game_over = True
        if winner == "Draw":
            status_label.config(text="It's a draw!")
        else:
            status_label.config(text=f"Player {winner} wins!")
        disable_all()
    else:
        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player, board, game_over
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    game_over = False
    status_label.config(text=f"Player {current_player}'s turn")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", state="normal", bg=default_btn_bg)

# --- UI setup ---
root = tk.Tk()
root.title("Tic Tac Toe")

# Use a larger font for buttons
btn_font = font.Font(size=24, weight="bold")

top_frame = tk.Frame(root)
top_frame.pack(padx=10, pady=10)

status_label = tk.Label(top_frame, text=f"Player {current_player}'s turn", font=("Helvetica", 14))
status_label.pack(pady=(0, 8))

grid_frame = tk.Frame(root)
grid_frame.pack()

# create buttons
default_btn_bg = tk.Button(root).cget("background")
for r in range(3):
    for c in range(3):
        b = tk.Button(grid_frame, text="", width=5, height=2, font=btn_font,
                      command=lambda rr=r, cc=c: on_click(rr, cc))
        b.grid(row=r, column=c, ipadx=8, ipady=8, padx=3, pady=3)
        buttons[r][c] = b

# control buttons
ctrl_frame = tk.Frame(root)
ctrl_frame.pack(pady=8)

reset_btn = tk.Button(ctrl_frame, text="Reset", command=reset_game)
reset_btn.pack(side="left", padx=6)

quit_btn = tk.Button(ctrl_frame, text="Quit", command=root.destroy)
quit_btn.pack(side="left", padx=6)

root.resizable(False, False)
root.mainloop()
