def isSafe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True
def solveNQueens(board, row, n):
    if row == n:
        for r in board:
            print(" ".join(r))
        print()
        return

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            solveNQueens(board, row + 1, n)
            board[row][col] = '.'  # Backtrack
# Driver Code
n = 4
board = [['.' for _ in range(n)] for _ in range(n)]
print(f"Solutions for {n}-Queens:\n")
solveNQueens(board, 0, n)