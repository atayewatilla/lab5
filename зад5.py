import numpy as np
import matplotlib.pyplot as plt

# Создаем фигуру с 3 областями
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# 1. Линейный график y = x^2
x = np.linspace(0, 10, 50)
ax1.plot(x, x**2, color='red')
ax1.set_title('y = x²')
ax1.grid()

# 2. Точечный график случайных точек
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
ax2.scatter(x_rand, y_rand, color='green')
ax2.set_title('Случайные точки')
ax2.grid()

# 3. Столбчатая диаграмма
categories = ['A', 'B', 'C']
values = [3, 7, 2]
ax3.bar(categories, values, color=['blue', 'orange', 'green'])
ax3.set_title('Категории')
ax3.grid(axis='y')

plt.tight_layout()  # Автоматическая настройка отступов
plt.show()