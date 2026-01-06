from config import SIZE, BOX_ROWS, BOX_COLS


def is_valid(board, row, col, num):
    # Check row
    for x in range(SIZE):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(SIZE):
        if board[x][col] == num:
            return False

    # Check 2x3 sub-grid
    start_row = row - row % BOX_ROWS
    start_col = col - col % BOX_COLS

    for i in range(BOX_ROWS):
        for j in range(BOX_COLS):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty(board):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, SIZE + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False
