class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []
 
    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
            if row - i - 1 >= 0 and self.board[row - i - 1][col - i - 1] == 1:
                return False
            if row + i + 1 < self.n and self.board[row + i + 1][col - i - 1] == 1:
                return False
        return True
 
    def solve_backtracking(self, col):
        if col >= self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
 
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.solve_backtracking(col + 1)
                self.board[i][col] = 0
 
        return False
 
    def solve_branch_and_bound(self, col):
        if col >= self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
 
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.solve_branch_and_bound(col + 1)
                self.board[i][col] = 0
 
        return False
 
    def print_solutions(self):
        for solution in self.solutions:
            print("Solution:")
            for row in solution:
                print(row)
            print()
 
 
# Example usage:
n_queens = NQueens(4)
print("Backtracking:")
n_queens.solve_backtracking(0)
n_queens.print_solutions()
 
n_queens = NQueens(4)
print("Branch and Bound:")
n_queens.solve_branch_and_bound(0)
n_queens.print_solutions()
