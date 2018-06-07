import matplotlib.pyplot as plt

x = list(range(1, 11))
y = [x**2 for x in x]

plt.plot(x, y)
plt.show()
