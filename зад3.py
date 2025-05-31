import numpy as np

# Создание матрицы 5x5 со случайными числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

print("Исходная матрица:")
print(matrix)

# Вычисление характеристик
mean_value = np.mean(matrix)          # Среднее значение
max_value = np.max(matrix)            # Максимальный элемент
min_value = np.min(matrix)            # Минимальный элемент
column_sums = np.sum(matrix, axis=0)  # Суммы по столбцам

print(f"\nСреднее значение: {mean_value:.2f}")
print(f"Максимальный элемент: {max_value}")
print(f"Минимальный элемент: {min_value}")
print(f"Суммы по столбцам: {column_sums}")