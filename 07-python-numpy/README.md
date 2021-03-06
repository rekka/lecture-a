
# Numerical math with Python

## `numpy`

Very fast arrays supporting vectorized operations similar to arrays in
Matlab.

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])
z = x + y
```

### References

- [Python Numpy Tutorial](http://cs231n.github.io/python-numpy-tutorial/)
- [100 numpy exercises with hint](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_hint.md)
- [Quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)


### Basic operations

Common to create arrays using `linspace`:

```python
x = np.linspace(0, 1, 11)
# x = array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])
```

Arrays have a type and a shape

```python
x.dtype         # = dtype('int64')
x.shape         # = (11,)
```

The shapes can be changed

```python
x = np.array([1, 2, 3, 4, 5, 6])

np.reshape(x, (3,2))

# 3 rows, 2 columns
# array([[1, 2],
#        [3, 4],
#        [5, 6]])

np.reshape(x, (2,3))

# 2 rows, 3 colums
# array([[1, 2, 3],
#       [4, 5, 6]])
```

Matrices are 2D arrays

```python
np.diag([1,2,3])

# array([[1, 0, 0],
#        [0, 2, 0],
#        [0, 0, 3]])
```

Other operations

  - transposition `x.T`
  - flattening `x.flatten()`
  - concatenating `np.concatenate([x, y])`
  - copying arrays `np.copy(x)`

Indexing operations are similar to lists

```python
a = np.reshape(np.arange(1, 10), (3, 3))

#  a = array([[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]])

                # 2nd row
a[1]            # = array([4, 5, 6])

                # 3rd column
a[:, 2]         # = array([2, 5, 8])
```

All indexing operations supported by lists: negative indices `a[-1]`,
ranges `a[1:-1]`, stepping `a[:, ::2]`.

### Vectorized operations

Instead of using a for loop, we can apply operations on many elements


```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])

z = x + y

s = np.sin(x**2 + 1) - y
```

Note: `x * y` is not the inner product!

```python
x * y                           #    = array([ 2,  6, 12])
x.dot(y)                        #    = 20

np.sum(x * y) == x.dot(y)       # = True
```

More advanced use cases are possible:

__Example.__  Set every other element to a given constant.

```python
x = np.zeros(10)
x[::2] = 1

# x = array([1., 0., 1., 0., 1., 0., 1., 0., 1., 0.])
```

### Conditions and filtering

Vectorized conditions

```python
x = np.arange(1, 11)

x > 5
# = array([False, False, False, False, False,
#          True,  True,  True, True, True])

np.sum(x > 5)           # = 5
```

`np.sum` returns the number of `True` elements since `True = 1` and
`False = 0` for addition.

Testing if all are `True` or at least one is `True`:

```
np.all(x > 5)           # = False

np.any(x > 5)           # = True
```

It is possible to index an array by an array of bools of the _same shape_.

```python
x[x > 5]
# = array([ 6,  7,  8,  9, 10])

x[x > 5] = 5
# = array([1, 2, 3, 4, 5, 5, 5, 5, 5, 5])
```

### Maximum and minimum

Maximum value `np.max` and the index of the first element with the maximum
value `np.argmax`.

```python
x = np.arange(1, 11)

np.max(x)                       # = 10

np.argmax(x)                    # = 9

x[np.argmax(x)] == np.max(x)    # = True
```

Element-wise maximum between multiple arrays.

```python
x = np.arange(1, 11)
y = np.arange(1, 11)[::-1]

np.maximum(x, y)
1

np.maximum(x, y)
# = array([10,  9,  8,  7,  6,  6,  7,  8,  9, 10])

np.minimum(x, y)
# = array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
```

Positive part of an array

```
x = np.linspace(-0.5, 0.5, 11)
np.maximum(x, 0)
# = array([0. , 0. , 0. , 0. , 0. , 0. , 0.1, 0.2, 0.3, 0.4, 0.5])
```

#### Exercise: better argmax function

Write an argmax function the returns the indices of all the maximum
values without using any for loop.

Example:

For array `np.array([1, 0, 1, 0, 1])`, the maximum 1 is located at indices 0, 2,
and 4. The return value of the argmax function should be `np.array([0,
2, 4])`.

Hint: `np.arange`


#### Exercise: Find an approximate solution of an equation

Find an approximate solution of exp(x) + x = 0 on the interval [-1, 1]
with accuracy 0.001.

Hint: `np.abs`, `np.argmin`

