# Data Analysis with NumPy, pandas and PySpark

Midterm coursework with four Python tasks (NumPy, pandas, Matplotlib) and one PySpark task that joins several tables. The parameters of each task (random seeds, months, row ranges) are derived from the student ID, so every student works on different values.

## What the project is

| Task | File | What it does |
|---|---|---|
| 1 | `L11_Tamele_70274_mid2/Task1.py` | Generates three random integer matrices of size 274 x 7,027 and compares them element by element (A against B, A against C, B against C), counting wins, losses and ties with vectorized NumPy operations. |
| 2 | `L11_Tamele_70274_mid2/Task2.py` | Creates 20 random points with 4 features, builds a pairwise distance matrix with a custom power-based distance, and finds each point's nearest neighbour. |
| 3 | `L11_Tamele_70274_mid2/Task3.py` | Loads daily Seattle weather for 2014 (`Seattle2014.csv`) with pandas, selects two months, and reports rainy days and the minimum, average, maximum and total precipitation. |
| 4 | `L11_Tamele_70274_mid2/Task4.py` | Takes a slice of `exam1_data.csv`, fits a degree-2 polynomial with `np.polyfit`, plots the data and curve with Matplotlib, and predicts five new random points (output: `task_4_plot_ET.png`). |
| 5 | `Colab/L11_Tamele_70274_mid2_.ipynb` | In PySpark, loads five related CSV files (`execution`, `person`, `dept`, `position`, `action`), joins them, filters the rows for one `id_20` value and computes the mean and standard deviation of time, cost and payment. |

## Goals

- Use NumPy vectorization instead of Python loops on large arrays.
- Practise reproducible randomness with fixed seeds.
- Clean and filter real data with pandas (dates, months, missing rainfall).
- Fit and visualize a simple regression model.
- Combine several tables with joins in Spark and compute summary statistics.

## Files

- `L11_Tamele_70274_mid2/`: Tasks 1 to 4 (`Task1.py` to `Task4.py`), the input data (`Seattle2014.csv`, `exam1_data.csv`), the five CSV tables for the PySpark task (semicolon-separated) and the plot from Task 4.
- `Colab/`: the PySpark task as a Colab notebook (`.ipynb`) and as a `.py` export.

## How to run

Tasks 1 to 4 (Python 3):

```bash
pip install numpy pandas matplotlib
cd L11_Tamele_70274_mid2
python Task1.py        # likewise Task2.py, Task3.py, Task4.py
```

Run the scripts from inside `L11_Tamele_70274_mid2`, because they read the CSV files by relative path.

PySpark task: open the notebook in **Google Colab**. It installs Java and PySpark, then reads the CSV files from a `Data.zip` archive. Create `Data.zip` from the five CSV files in `L11_Tamele_70274_mid2` (`execution`, `person`, `dept`, `position`, `action`) and upload it to the Colab session, or edit the paths in the notebook.

## What can be learned from it

- **Vectorization:** comparing millions of values with one NumPy expression is far faster and shorter than looping.
- **Reproducibility:** why `np.random.seed` makes results repeatable and checkable.
- **Distance matrices and nearest neighbours:** the basis of many machine learning methods such as k-nearest neighbours.
- **Working with dates and real data in pandas:** parsing dates, filtering by month, handling zero values.
- **Polynomial regression:** fitting a curve, using it to predict new points and judging the fit on a plot.
- **Joins at scale:** combining five related tables on their keys and aggregating the result with Spark.
