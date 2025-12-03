# Reads multi-line Sudoku input until two consecutive blank lines are entered
def get_big_input():
    lines = []
    while True:
        line = input()
        if line == "":
            if lines and lines[-1] == "":
                break
            else:
                lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines).strip()

# Parses multiple Sudoku puzzles from a single input string
def parse_sudokus(big_input):
    puzzles = big_input.strip().split("Grid ")
    boards = []
    for puzzle in puzzles:
        if not puzzle.strip():
            continue
        lines = puzzle.strip().splitlines()
        if lines[0].isdigit() or lines[0][:2].isdigit():
            lines = lines[1:]
        board = [[int(ch) for ch in line] for line in lines]
        boards.append(board)
    return boards

# Finds the next empty cell in the Sudoku board
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Checks if placing a number at a given position is valid
def valid(board, num, pos):
    row, col = pos

    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

# Solves the Sudoku board using backtracking
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Finds the 3-digit number formed by the top-left 3 cells of the solved board
def find_top_3(board):
    return sum(int(board[0][i]) * 10**(2-i) for i in range(3))

# Solves all Sudoku puzzles and computes the sum of their top-3 values
def solve_all(big_input):
    boards = parse_sudokus(big_input)
    total = 0
    for idx, board in enumerate(boards, start=1):
        solve(board)
        top3 = find_top_3(board)
        total += top3
        print(f"Top 3 digits for GRID{idx}: {top3}")
    print("\nFinal sum of all top-3 values:", total)
    return total


if __name__ == "__main__":
    all_sudoku_inputs = get_big_input()  # Inputs all Sudoku puzzles
    solve_all(all_sudoku_inputs)         # Solves and prints results (top left 3 numbers as a number) and the sum of them all