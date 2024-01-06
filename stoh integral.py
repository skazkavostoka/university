import numpy as np

# Заданные параметры распределений
mean_v1, std_v1 = 2, 1
mean_v2, std_v2 = 4, 1
low_v3, high_v3 = 0, 2

# Количество выборок
N = 10000

# Генерация случайных векторов
v1 = np.random.normal(mean_v1, std_v1, N)
v2 = np.random.normal(mean_v2, std_v2, N)
v3 = np.random.uniform(low_v3, high_v3, N)

# Вычисление значений функции для каждого вектора
f_x = np.sqrt(v1**2 + v2**2 + v3**2)

# Вычисление стохастического интеграла
L = np.mean(f_x)

print(f"Значение стохастического интеграла L: {L}")