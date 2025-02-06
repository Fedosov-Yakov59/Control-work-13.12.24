import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, np.sin(x), 'r-', label='sin(x)')
plt.plot(x, np.cos(x), 'g--', label='cos(x)')
plt.plot(x, np.tan(x), 'b:', label='tan(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций sin(x), cos(x) и tan(x)')
plt.show()
