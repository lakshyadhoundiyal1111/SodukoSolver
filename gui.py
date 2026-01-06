from tkinter import *
from tkinter import messagebox
from solver import solve_sudoku
from config import SIZE, BOX_ROWS, BOX_COLS
from puzzles import PUZZLES
import random
import copy


def start_gui():
    root = Tk()
    root.title("6x6 Sudoku Solver")

    cells = []

    # Pick one random puzzle
    PUZZLE = random.choice(PUZZLES)

    # Create solved board for validation
    solution_board = copy.deepcopy(PUZZLE)
    solve_sudoku(solution_board)

    # ---------------- HELPER FUNCTIONS ----------------

    def get_board():
        board = []
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                val = cells[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_board(board):
        for i in range(SIZE):
            for j in range(SIZE):
                cells[i][j].config(state="normal")
                cells[i][j].delete(0, END)
                cells[i][j].config(fg="black")

                if board[i][j] != 0:
                    cells[i][j].insert(0, board[i][j])

                # Lock original puzzle cells again
                if PUZZLE[i][j] != 0:
                    cells[i][j].config(state="disabled")

    # ---------------- BUTTON LOGIC ----------------

    def submit():
        board = get_board()
        error_found = False

        for i in range(SIZE):
            for j in range(SIZE):
                # Skip original fixed cells
                if PUZZLE[i][j] != 0:
                    continue

                cells[i][j].config(fg="black")

                if board[i][j] == 0:
                    continue

                if board[i][j] != solution_board[i][j]:
                    cells[i][j].config(fg="red")
                    error_found = True

        if error_found:
            messagebox.showerror(
                "Incorrect Sudoku",
                "Some numbers are incorrect.\nThey are highlighted in red."
            )
        else:
            messagebox.showinfo(
                "Success",
                "Congratulations! All entered numbers are correct."
            )

    def solve():
        board = get_board()
        if solve_sudoku(board):
            set_board(board)
        else:
            messagebox.showerror("No Solution", "No solution exists.")

    def clear():
        for i in range(SIZE):
            for j in range(SIZE):
                if PUZZLE[i][j] == 0:
                    cells[i][j].config(state="normal")
                    cells[i][j].delete(0, END)
                    cells[i][j].config(fg="black")

    # ---------------- CREATE GRID ----------------

    for i in range(SIZE):
        row_cells = []
        for j in range(SIZE):
            e = Entry(
                root,
                width=4,
                font=("Arial", 18),
                justify="center"
            )
            e.grid(row=i, column=j, padx=3, pady=3)

            if PUZZLE[i][j] != 0:
                e.insert(0, PUZZLE[i][j])
                e.config(state="disabled", disabledforeground="black")

            row_cells.append(e)
        cells.append(row_cells)

    # ---------------- BUTTONS ----------------

    Button(root, text="Submit", command=submit, width=10).grid(
        row=SIZE, column=0, columnspan=2, pady=10
    )

    Button(root, text="Solve", command=solve, width=10).grid(
        row=SIZE, column=2, columnspan=2, pady=10
    )

    Button(root, text="Clear", command=clear, width=10).grid(
        row=SIZE, column=4, columnspan=2, pady=10
    )

    root.mainloop()
