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
