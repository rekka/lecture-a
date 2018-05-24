# Intro to Python

We use Python 3.

You can install it using
[Anaconda](https://www.anaconda.com/download/)

## Learning

Use documentation available at: <https://docs.python.org/3/>

## Running code

Python interpreter

```bash
$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

and you can run commands interactively.

Or you save them into a file `file.py` and run using `python file.py`.

```python
# comment
n = 10
s = sum(range(11))
print("sum =", s)
```

`print`
: printing

`n = 10`
: assign value `10` to variable `n`

`sum`
: sum of a list or any collection

`range`
: produces a sequence

## `jupyter`

`jupyter` allows running Python interactively with outputs inline.

```bash
$ jupyter notebook
```

starts a server and open a webpage in the browser.

Click `New` and then `Notebook Python 3` to create a new _notebook_.

### Basic commands

`Shift+Enter`
: execute cell

`Esc`
: exit cell

`x`
: cut cell (deletes cell)

`c`
: copy cell

`v`
: paste cell

`Shift+Tab`
: while editing, shows help on the function under the cursor

## Functions

`print`, `sum` and `range` are functions.

Functions are values:

```python
p = print
p("hey")
```

This can be used to do _functional programming_ in Python.

Sum of sublists:
```python
list(map(sum, [[1,2], [3, 4, 6], [9,2]]))
```

## Lists

```python
ls = [1,2,3,4,5]
```

Indexing

```python
ls[3]       # 4-th element
ls[-1]      # the last element
ls[::2]     # every other element
ls[1::2]    # every other element, but skip the first
ls[::-1]    # reversed list
```

__Note:__ All variables in Python are __pointers__ to values.

```python
other = ls
```

makes variable `other` point to the same list as variable `ls`.

Therefore `ls[2] = 1000` will change `other[2]` as well.

To create a copy of the list, use

```python
other = list(ls)
```

## List comprehensions

```python
ls = [[1,2], [3, 4, 6], [9,2]]

# averages of all sublists
[sum(i) / len(i) for i in ls]
```

```python
ls = [[1,2], [], [3, 4, 6], [], [9,2]]

# averages of only the nonempty sublists
[sum(i) / len(i) for i in ls if len(i) > 0]
```

```python
v = [1, 2, 3]
w = [0.4, 6, 3]

# product of all 9 pairs of the
[x * y for x in v for y in w]
```


