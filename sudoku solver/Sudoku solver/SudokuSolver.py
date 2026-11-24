
#Sudoku Solver

#this class solves The sudoku puzzles using backtracking.
#the ideas used in order to solve this is  linear search and least candidates search.


class SudokuSolver:
    # initialize solver with standard Sudoku size
    def __init__(self):
        self.size = 9          # 9x9 grid
        self.subgrid_size = 3  # 3x3 boxes
    
    # check if number can go in a cell
    def _is_valid(self, grid, row, col, num):
        for c in range(self.size):
            if grid[row][c] == num:
                return False
        
        # check the column
        for r in range(self.size):
            if grid[r][col] == num:
                return False
        
        # check 3x3 box
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size
        
        for r in range(start_row, start_row + self.subgrid_size):
            for c in range(start_col, start_col + self.subgrid_size):
                if grid[r][c] == num:
                    return False
        
        return True
    
    # find next empty cell (row by row)
    def _find_empty_linear(self, grid):
        for r in range(self.size):
            for c in range(self.size):
                if grid[r][c] == 0:
                    return r, c
        return None, None  # no empty cells means the puzzle solved!
    
    # count how many numbers could go in a cell
    def _count_candidates(self, grid, row, col):
        if grid[row][col] != 0:  # cell already filled
            return 0
        
        count = 0

        # try numbers 1 through 9
        for num in range(1, 10):
            if self._is_valid(grid, row, col, num):
                count += 1
        return count
    
    # find cell with fewest possible numbers
    def _find_empty_least_candidates(self, grid):
        min_candidates = 10  # start with high number
        best_cell = (None, None)
        
        for r in range(self.size):
            for c in range(self.size):
                if grid[r][c] == 0:
                    candidates = self._count_candidates(grid, r, c)
                    # if only 1 possible number, use this cell
                    if candidates == 1:
                        return r, c
                    # track cell with fewest options
                    if candidates < min_candidates:
                        min_candidates = candidates
                        best_cell = (r, c)
        
        return best_cell
    
    # backtracking solver trying numbers until a correct solution is found 
    def _backtrack(self, grid, order='lin'):
        # pick next cell based on ('lin')
        if order == 'lin':
            row, col = self._find_empty_linear(grid)
        else:  #lnc method being used
            row, col = self._find_empty_least_candidates(grid)
        
        # if no empty cells, we're done
        if row is None:
            return True
        
        # try numbers 1-9 in this cell
        for num in range(1, 10):
            if self._is_valid(grid, row, col, num):
                grid[row][col] = num 
                # try to solve rest of puzzle
                if self._backtrack(grid, order):
                    return True
                grid[row][col] = 0  # backtrack if stuck
        
        return False  # no number worked in this cell
    
    # main solve method - public interface
    def solve(self, grid, order='lin'):
        # check order parameter
        if order not in ['lin', 'lnc']:
            raise ValueError("Use 'lin' or 'lnc' for order")
        
        # make copy so we don't change original
        solution = [row.copy() for row in grid]
        
        # attempt to solve
        if self._backtrack(solution, order):
            return solution
        return None  # no solution exists
    
    # print puzzle in nice format
    def print_grid(self, grid):
        for i in range(self.size):
            # draw horizontal line every 3 rows
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(self.size):
                # draw vertical line every 3 columns
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                # print number or dot for empty
                print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
            print()


# test the solver
if __name__ == "__main__":
    import time
    
    solver = SudokuSolver()
    

    print("ERICS SUDOKU SOLVER TEST")

    # test 1: example
    print("\n1. EXAMPLE PUZZLE")
    
    example_puzzle = [
        [0, 0, 0, 0, 1, 0, 0, 2, 0],
        [1, 0, 0, 7, 0, 2, 0, 8, 0],
        [2, 5, 7, 0, 0, 0, 0, 0, 0],
        [6, 1, 2, 0, 0, 7, 0, 4, 3],
        [0, 0, 5, 0, 0, 0, 6, 0, 0],
        [9, 7, 0, 6, 0, 0, 2, 1, 8],
        [0, 0, 0, 0, 0, 0, 1, 3, 4],
        [0, 8, 0, 5, 0, 3, 0, 0, 7],
        [0, 9, 0, 0, 6, 0, 0, 0, 0]
    ]
    
    print("\nOriginal puzzle:")
    solver.print_grid(example_puzzle)
    
    print("\nSolving with linear strategy (order='lin'):")
    start = time.time()
    solution_lin = solver.solve(example_puzzle, order='lin')
    end = time.time()
    
    if solution_lin:
        solver.print_grid(solution_lin)
        print(f"\nSolved in {end - start:.4f} seconds")
    else:
        print("No solution found")
    
    print("\nSolving with least candidates strategy (order='lnc'):")
    start = time.time()
    solution_lnc = solver.solve(example_puzzle, order='lnc')
    end = time.time()
    
    if solution_lnc:
        solver.print_grid(solution_lnc)
        print(f"\nSolved in {end - start:.4f} seconds")
    else:
        print("No solution found")
    
    if solution_lin and solution_lnc and solution_lin == solution_lnc:
        print("\nBoth strategies produced the same solution")
    

    # test 2: low difficulty
    print("2. LOW DIFFICULTY PUZZLE:")

    # create and then hide some numbers
    low_puzzle = [
        [9, 8, 1, 2, 3, 4, 7, 6, 5],
        [6, 4, 7, 1, 8, 9, 5, 3, 2],
        [3, 2, 5, 6, 7, 9, 1, 4, 8],
        [7, 1, 3, 4, 6, 2, 8, 5, 9],
        [2, 9, 4, 7, 5, 3, 1, 2, 8],
        [5, 6, 8, 9, 1, 7, 4, 2, 3],
        [4, 5, 6, 3, 9, 8, 2, 7, 1],
        [8, 3, 2, 5, 4, 1, 9, 6, 7],
        [1, 7, 9, 8, 2, 6, 3, 5, 4]
    ]

    # hide most numbers to create puzzle
    for i in range(9):
        for j in range(9):
            if (i + j) % 3 != 0:
                low_puzzle[i][j] = 0
    
    print("\nOriginal low difficulty puzzle:")
    solver.print_grid(low_puzzle)
    
    print("\nSolving with least candidates strategy (order='lnc'):")
    start = time.time()
    solution_low = solver.solve(low_puzzle, order='lnc')
    end = time.time()
    
    if solution_low:
        solver.print_grid(solution_low)
        print(f"\nSolved in {end - start:.4f} seconds")
        if end - start < 180:
            print("Meets requirement: solved in under 180 seconds")
    else:
        print("No solution found")
    
    # test 3: medium difficulty
    print("3. Medium DIFFICULTY PUZZLE:")
    
    moderate_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("\nOriginal medium difficulty puzzle:")
    solver.print_grid(moderate_puzzle)
    
    print("\nSolving with linear strategy (order='lin'):")
    start = time.time()
    solution_moderate = solver.solve(moderate_puzzle, order='lin')
    end = time.time()
    
    if solution_moderate:
        solver.print_grid(solution_moderate)
        print(f"\nSolved in {end - start:.4f} seconds")
        if end - start < 180:
            print("Meets requirement: solved in under 180 seconds")
    else:
        print("No solution found")
    
    # test 4: hard puzzle
    print("4. HIGH DIFFICULTY PUZZLE:")

    high_puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]
    
    print("\nOriginal high difficulty puzzle:")
    solver.print_grid(high_puzzle)
    
    print("\nSolving with least candidates strategy (order='lnc'):")
    start = time.time()
    solution_high = solver.solve(high_puzzle, order='lnc')
    end = time.time()
    
    if solution_high:
        solver.print_grid(solution_high)
        print(f"\nSolved in {end - start:.4f} seconds")
        if end - start < 180:
            print("Meets requirement: solved in under 180 seconds")
    else:
        print("No solution found")