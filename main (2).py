import matplotlib.pyplot as plt

x = ['Яблоки', 'Бананы', 'Апельсины', 'Груши']
y = [10, 15, 7, 12]

plt.bar(x, y)
plt.xticks(x)
plt.ylabel("Количество")
plt.title("Количество фруктов")
plt.show()