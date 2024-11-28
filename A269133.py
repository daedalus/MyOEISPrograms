# Code for A269133
# Author Darío Clavijo, 2024.

def solve_k_queens(n, k, row=0, board=None, solutions=None):
    def is_safe(board, row, col, n):
        # Check column for attacks
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    if solutions is None: solutions = []
    if board is None: board = [-1] * n  # Initialize board
    # If k queens are placed, add the solution
    if k == 0:
        solutions.append(board[:])
        return solutions
    # If we've placed queens in all rows or k queens are placed
    if row == n: return solutions
    # Try placing a queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            # Place queen and continue to next row
            solve_k_queens(n, k - 1, row + 1, board, solutions)
            # Backtrack
            board[row] = -1
    return solutions
row = lambda n: [len(solve_k_queens(n, k)) for k in range(1,n+1)]

A=[]
for n in range(1,12):
  A+=row(n)
print(A)
