# Will work for varying sizes of chessboard starting from 4x4
def print_board(board):
    """Print the chessboard configuration."""
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def solveNQueens(board, col):
    """using backtracking to solve the N Queens problem."""
    if col == N:
        print_board(board)
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def isSafe(board, row, col):
    for x in range(col): # check this row on left side
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)): # check upper diagonal on left side
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)): # check lower diagonal on left side
        if board[x][y] == 1:
            return False
    return True

if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard (e.g., 8 for 8-Queens): "))
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solveNQueens(board, 0):
        print("No solution found")