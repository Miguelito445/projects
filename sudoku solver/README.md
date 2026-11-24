# Backtracking Sudoku Solver with Search Heuristics

A Sudoku solver in Python that uses **recursive backtracking** and lets you compare two strategies for choosing the next cell to fill.

## What the project is

`SudokuSolver` solves a standard 9x9 Sudoku. A puzzle is a list of 9 lists of integers, where `0` means an empty cell.

```python
solver = SudokuSolver()
solution = solver.solve(puzzle, order='lnc')   # returns a solved copy, or None if there is no solution
solver.print_grid(solution)
```

The `order` argument selects the search strategy:

| Strategy | Meaning | How it picks the next cell |
|---|---|---|
| `'lin'` | Linear search | The first empty cell, row by row |
| `'lnc'` | Least candidates | The empty cell with the fewest valid numbers (a cell with exactly one option is taken immediately) |

The original puzzle is never modified, because the solver works on a copy.

## Goals

- Implement the solver with backtracking: try a number, recurse, and undo it if the branch fails.
- Compare a simple search order with a smarter heuristic.
- Solve puzzles of increasing difficulty within the time limit of the task (180 seconds).

## Results

Measured in a test run (timings depend on your machine):

- Medium puzzle: solved in about 0.02 s with `'lin'` and almost instantly with `'lnc'`.
- Hard puzzle (very few given numbers): solved in about **9 seconds** with `'lnc'`. The `'lin'` strategy did not finish within several minutes on the same puzzle, which shows how much the heuristic helps.

## Files

- `SudokuSolver.py`: the `SudokuSolver` class and four test puzzles (example, "low difficulty", medium, high difficulty).

## How to run

Requires Python 3 only (no external packages).

```bash
python SudokuSolver.py
```

The hard puzzle is solved with `'lnc'` only. Do not run it with `'lin'` unless you are prepared to wait a long time.

## Known issue

The "low difficulty" test puzzle is built by hiding cells of a grid that is not a valid solved Sudoku (some columns contain repeated numbers). The solver therefore correctly reports **"No solution found"** for that test. The solver itself is not at fault; replacing the base grid with a valid solved board would fix the test.

## What can be learned from it

- **Backtracking:** exploring choices, undoing them when they lead to a dead end, and returning success or failure up the recursion.
- **Constraint checking:** validating a number against its row, column and 3x3 box.
- **Heuristics for pruning:** choosing the most constrained cell first reduces the number of branches dramatically (the same idea as the "minimum remaining values" heuristic in constraint-satisfaction problems).
- **Comparing algorithms empirically:** timing two strategies on the same inputs and interpreting the difference.
- **Defensive design:** validating the `order` argument and not mutating the caller's data.
