import numpy as np
import matplotlib.pyplot as plt

# Генерация 1000 случайных чисел с нормальным распределением
data = np.random.normal(loc=0, scale=1, size=1000)  # loc - среднее, scale - СКО

# Построение гистограммы
plt.figure(figsize=(10, 5))
plt.hist(data, bins=20, color='green', edgecolor='black')  # 20 столбцов

# Оформление
plt.title('Гистограмма нормального распределения')  # Заголовок
plt.xlabel('Значения')                             # Подпись оси X
plt.ylabel('Частота')                              # Подпись оси Y
plt.grid(axis='y')                                 # Сетка только по Y
plt.show()