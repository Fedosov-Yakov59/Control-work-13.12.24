import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(size=1000)
plt.hist(data, bins=20)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма случайных данных')
plt.show()

