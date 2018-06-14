# Numerical math with Python

## numpy arrays

Review [the notes from last
week](https://github.com/rekka/lecture-a/tree/master/07-python-numpy).

### Random arrays

Module `numpy.random`.

Uniform distribution over `[0,1]` with `numpy.random.rand`:

```python
np.random.rand(3,2)

# = array([[0.34017747, 0.20074433],
#          [0.76708278, 0.2682637 ],
#          [0.18338039, 0.3142762 ]])
```

### Exercise: Estimate π using the Monte-Carlo method

The are of the disc _D_ with radius 1 is exactly π. The are of the
square _Q_ with edge of size 2 is 4. Let us center both of these at the
origin (0,0). Then _D_ ⊂ _Q_. If we generate a sequence of uniformly
distributed point in _Q_, approximately π/4 should be in _D_. Use this
to estimate the value of π. Use 10, 100, 1000, 1000000 points.

Hint: Use `np.random.rand`, conditions to check if a point is in a disc,
counting True values using `np.sum`.

### Exercise: Monte-Carlo integration

Integrate the function `(1 - x**2)**(1/2)` over the interval [-1, 1]
using the Monte-Carlo method: Generate uniformly distributed samples
over the interval [-1, 1] and compute the average of the function values
evaluated at the samples. This values should converge to the value of
the integral divided by the length of the interval.
Use 10, 100, 1000, 1000000 samples.

Hint: `np.sqrt` or `**0.5` for square root.

## Plotting with `matplotlib`

```python
import matplotlib.pyplot as plt

x = list(range(1, 11))
y = [x**2 for x in x]

plt.plot(x, y)
plt.show()
```

Works great with numpy arrays:

```python
x = np.arange(1, 11)
y = x**2

plt.plot(x, y)
plt.show()
```

Change markers

```python
plt.plot(x, y, 'o:')
plt.show()
```

Remove the line altogether and set the aspect ratio to 1:1 ('equal').

```python
x = np.random.rand(10)
y = np.random.rand(10)
plt.subplot(111, aspect = 'equal')
plt.plot(x, y, '.')
```

### Exercise

Plot the function and the random samples from exercise Monte-Carlo
integration above.

### Exercise

Solve the system

```
x' = -y
y' = x
x(0) = 1
y(0) = 0
```

using explicit Euler's method and plot the solution for different time
steps 1, 0.1, 0.01.
