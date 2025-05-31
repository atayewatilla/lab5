import numpy as np
import matplotlib.pyplot as plt

# Используем матрицу из задания 3
matrix = np.random.randint(1, 11, size=(5, 5))

# Создание тепловой карты
plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='viridis')  # Карта с цветовой схемой 'viridis'
plt.colorbar(label='Значения')      # Цветовая шкала

# Добавление аннотаций
for i in range(matrix.shape[0]):    # По строкам
    for j in range(matrix.shape[1]): # По столбцам
        plt.text(j, i, matrix[i, j], 
                ha='center', va='center',
                color='white')

# Оформление
plt.title('Тепловая карта матрицы 5x5')
plt.xticks(range(5))
plt.yticks(range(5))
plt.show()