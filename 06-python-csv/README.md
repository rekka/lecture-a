
Data processing in Python.

# Loading CSV files

Use the [`csv` module](https://docs.python.org/3/library/csv.html).

We will try to read the file
[`US_births_2000-2014_SSA.csv`](https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv)
from [FiveThirtyEight](https://data.fivethirtyeight.com/).

Download the file first to the same folder as your python script.
To read all the rows as lists, use

```python
import csv

with open('US_births_2000-2014_SSA.csv') as f:
    data = list(csv.reader(f))

print(data[:10])
```

The first row are the names of the fields.

It is more convenient to work with entries as dictionaries:

```python
import csv

with open('US_births_2000-2014_SSA.csv') as f:
    data = list(csv.DictReader(f))

print(data[:10])
```

## Exercises

1. Convert the numbers from strings to an int.

    Hint: Function `int`.

2. What is the total number of births each year (2000--2014)?

3. Which month/day of the way has the most births overall/at each given
   year?

# Basic plotting with `matplotlib`

```python
import matplotlib.pyplot as plt

x = list(range(1, 11))
y = [x**2 for x in x]

plt.plot(x, y)
plt.show()
```

## Exercises

1. Plot the number of births in a given year as the function of year.

