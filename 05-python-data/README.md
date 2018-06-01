# Exercise 1
Given a list of numbers, produce a list with numbers sorted.

```python
x = [5,1, 4,6,9]

sorted(x)
````

Bubble sort

```python
for i in range(len(x) - 1):
    for j in range(i + 1, len(x)):
        if x[j] < x[i]:
            t = x[i]
            x[i] = x[j]
            x[j] = t
```

# Strings

```python
s = 'string'
```

Strings are just lists of characters

```python
s[::2]
```

## Comparing strings manually

```python
def str_compare(s, t):
    if len(s) != len(t):
        return False

    for i, j in zip(s, t):
        if i != j:
            return False

    return True
```

# Sets

Collection of unique elements

```python
{1, 2, 8, 4, 5, 4, 1}
```

# Dictionaries

```python
d  = {"x": 0.1, "y": 0.5}
d["z"] = [5,5,5]
```

Comprehensions

```python
f = {x: x**2 for x in x}
```

## Exercise: number of occurrences

Find the dictionary of distinct elements in a given list with the number
of occurrences of each.

```python
from random import randint

x = [randint(0, 10) for i in range(100)]


d = {}
for v in x:
    if not v in d:
        d[v] = 0

    d[v] += 1
d
```

## Quicksort

```python
def quicksort(x):
    if len(x) <= 1:
        return x
    pivot = x[0]
    return quicksort([v for v in x if v < pivot])\
    + [v for v in x if v == pivot]\
    + quicksort([v for v in x if v > pivot])
```

# Exercises

## Full inverse of a dictionary

For a dictionary

```python
>>> d = {x: x**2 for x in range(10)}
>>> d
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

the "inverse" is the dictionary

```python
>>> {v: k for k, v in d.items()}
{0: 0, 1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7, 64: 8, 81: 9}
```

However, the above works well only if every value has exactly one key
that maps to it.

```python
>>> d = {x: x**2 for x in range(-5, 5)}
>>> d
{-5: 25, -4: 16, -3: 9, -2: 4, -1: 1, 0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>> {v: k for k, v in d.items()}
{25: -5, 16: 4, 9: 3, 4: 2, 1: 1, 0: 0}
```

Notice that above we are missing some value -> key mappings.

1. Write a function that finds the _full inverse_ of a given dictionary:

    ```python
    >>> d = {x: x**2 for x in range(-5, 5)}
    >>> full_inverse(d)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3], 16: [-4, 4], 25: [-5]}
    ```
2. Write a function that takes two dictionaries and returns `True`
   exactly when the second is the full inverse of the first one.
   Since this function is meant for testing the previous one, do **not** use
   the following code.

    ```python
    def check_full_inverse(d, i):
        return i == full_inverse(d)
    ```


