import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100000)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции y = sin(x)")
plt.grid(True)

plt.show()