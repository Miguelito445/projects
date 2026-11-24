# Cars Data Analysis with PySpark (DataFrames, Spark SQL and RDDs)

Lab coursework that solves the same data tasks in three ways in Apache Spark: the **DataFrame API**, **Spark SQL** and low-level **RDD** transformations.

## What the project is

A Google Colab notebook (`L10_Tamele_70274_car2_RDD.ipynb`, also exported as a `.py` file) with numbered exercises (1 to 14).

**Part 1: a cars dataset (columns include Car, MPG, Cylinders, Horsepower, Weight, Origin).** Each exercise is solved twice, once with DataFrames (a) and once with SQL (b):

- Left join with a small reference table to turn origin codes into full names.
- Cross join with a table of weight ranges, then a filter, to assign each car a weight class (Light, Medium, Heavy, Very Heavy).
- Group-by statistics per origin: mean, median and standard deviation of MPG and Weight, rounded to two decimals.
- Distinct values, min/max/average MPG for 4, 6 and 8 cylinders, and filters such as MPG equal to 0 or above 46.

**Part 2: Python and RDDs.**

- Lambda functions with `map()` and `filter()`.
- Creating a `SparkContext`, parallelizing a list, and using `collect`, `take`, `first` and `count`.
- Loading a text file (`shakespeare.txt`) as an RDD, splitting lines into words with `map` and `flatMap`, and removing English stop words (NLTK) with `filter`.

## Goals

- Learn how to express the same query in the DataFrame API and in SQL, and see that they give the same result.
- Practise joins, aggregations and filters on tabular data.
- Understand the difference between `map` and `flatMap` and how an RDD pipeline works.

## Files

- `L10_Tamele_70274_car2_RDD.ipynb`: the notebook with the exercises and explanations.
- `l10_tamele_70274_car2_rdd.py`: the same code exported from Colab as a script.

## How to run

The notebook is meant for **Google Colab**. It continues a larger lab, so it needs the following before Exercise 1a:

1. A Spark session and PySpark installed (`pip install pyspark` and Java in Colab).
2. The cars dataset loaded into a DataFrame and registered as a SQL view named `cars`.
3. The file `shakespeare.txt` in the working directory (for the RDD exercises).

These setup steps and the data files are not included in this folder.

## What can be learned from it

- **DataFrame API versus Spark SQL:** two interfaces to the same engine, and when each reads more clearly.
- **Joins:** a left join for lookups and a cross join with a range filter for "bucketing" values into classes.
- **Aggregations:** grouping and computing statistics, including a median with `percentile`.
- **RDD basics:** transformations (`map`, `flatMap`, `filter`) versus actions (`count`, `take`, `collect`), and how text processing is done with them.
- **Text cleaning:** tokenizing and removing stop words before counting words.
