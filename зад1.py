import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)  # Синусоида
z = np.cos(x)  # Косинусоида

# Создание графика
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)', color='blue')  # График синуса
plt.plot(x, z, label='cos(x)', color='red')   # График косинуса

# Оформление
plt.title('Графики функций sin(x) и cos(x)')  # Заголовок
plt.xlabel('Ось X')                          # Подпись оси X
plt.ylabel('Ось Y')                          # Подпись оси Y
plt.legend()                                 # Легенда
plt.grid()                                   # Сетка
plt.show()