# 🧩 Sudoku Solver (6×6) — Python & DSA

A **6×6 Sudoku Solver application** built using **Python**, **Tkinter**, and **Data Structures & Algorithms (Backtracking)**.  
The project demonstrates clean algorithmic thinking, modular design, and a user-friendly GUI.

---

## 📌 Overview

This application allows users to:
- Solve a **6×6 Sudoku puzzle** interactively
- Validate their solution using a **Submit** button
- Automatically solve the puzzle using a **backtracking algorithm**

The project is structured to clearly separate:
- **Algorithm logic**
- **GUI logic**
- **Configuration**
- **Puzzle data**

---

## ✨ Features

- ✅ 6×6 Sudoku grid (with **2×3 sub-grids**)
- 🎲 Randomly selected pre-filled puzzles
- ✍️ User input for empty cells
- 🔴 Incorrect entries highlighted in **red**
- 📢 Single error message on submission if mistakes exist
- 🤖 Automatic solving using **backtracking**
- 🔒 Pre-filled cells are locked (non-editable)
- 🧹 Clear, Solve, and Submit functionality
- 🖥️ Desktop GUI using Tkinter

---

## 🧠 DSA Concepts Used

- **Backtracking**
- **Recursion**
- **Constraint Satisfaction Problem (CSP)**
- **2D Matrix Representation**
- **State Restoration (Undo / Backtrack)**

The solver tries valid numbers recursively and backtracks when a constraint is violated.

---

## 🏗️ Project Structure

Sudoku solver/
|-- main.py     -> Application entry point
|-- gui.py      -> Tkinter graphical interface
|-- solver.py   -> Backtracking Sudoku solver (DSA logic)
|-- puzzles.py  -> Pre-filled Sudoku puzzles
|-- config.py   -> Configuration constants
`-- README.md   -> Project documentation




In this structure:
- `main.py` serves as the starting point of the application.
- `gui.py` handles all user interface functionality using Tkinter.
- `solver.py` contains the core backtracking algorithm.
- `puzzles.py` stores multiple predefined Sudoku boards.
- `config.py` centralizes configuration values such as grid size and sub-grid dimensions.
- `README.md` provides documentation for the project.

---

## ▶️ How to Run

Ensure Python is installed on your system, then run the application using:

```bash
python main.py


