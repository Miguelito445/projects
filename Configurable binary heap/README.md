# Configurable Binary Heap (Min/Max) in Python

A binary heap implemented from scratch in Python that can work as either a **min-heap** or a **max-heap**, with an O(n) bulk-build method.

## What the project is

`BinHeap` is a class that stores a binary heap in a plain Python list (array-based tree). The heap type is chosen when the object is created: `BinHeap('min')` (default) or `BinHeap('max')`.

| Method | What it does | Time complexity |
|---|---|---|
| `build(lst)` | Builds a heap from a list using Floyd's algorithm | O(n) |
| `insert(x)` | Adds an element and moves it up to its place | O(log n) |
| `pop()` | Removes and returns the top element | O(log n) |
| `top()` | Returns the top element without removing it | O(1) |
| `len(heap)`, `str(heap)` | Size and printable form | O(1) / O(n) |

Invalid input is handled with errors: an unknown heap type raises `ValueError`, and `top()` or `pop()` on an empty heap raises `IndexError`.

## Goals

- Implement a heap without using Python's `heapq` module.
- Support both min and max behaviour in one class.
- Build a heap from 1,000,000 elements in **under 3 seconds** (the task requirement).
- Verify correctness with tests, including a check of the heap property.

## Results

In a test run, building a heap from 1,000,000 random integers took about **0.4 seconds**, and the full heap-property check passed. Timings depend on your machine.

## Files

- `Binary_heap.py`: the `BinHeap` class plus a test section with the expected outputs from the task.
- `performance_test.py`: generates 1,000,000 random numbers, times `build()` and checks the result.

## How to run

Requires Python 3 only (no external packages).

```bash
python Binary_heap.py        # runs the correctness tests
python performance_test.py   # runs the 1,000,000-element timing test
```

Run both files from inside this folder, because `performance_test.py` imports `Binary_heap.py`.

## What can be learned from it

- **How a binary heap works:** the parent/child index rules (`2i+1`, `2i+2`, `(i-1)//2`) and why a tree can live in a flat array.
- **Heapify up and down:** the two operations that keep the heap property after an insert or a removal.
- **Why building a heap is O(n):** Floyd's method starts at the last non-leaf node and heapifies downward, which is faster than inserting n elements one by one (O(n log n)).
- **Writing a configurable class:** one implementation serving two behaviours, with validation and clear errors.
- **Performance testing:** measuring a requirement with a realistic input size and verifying the output, not only timing it.
