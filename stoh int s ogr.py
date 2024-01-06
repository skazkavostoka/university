import numpy as np
from math import


# Заданные параметры распределений
mean_v1, std_v1 = 4, 2
mean_v2, std_v2 = 0, 1
exp_v3 = 2
low_v4, high_v4 = 1, 4
# Количество выборок
N = 10000
# Генерация случайных векторов
v1 = np.random.normal(mean_v1, std_v1, N)
v2 = np.random.normal(mean_v2, std_v2, N)
v3 = np.random.exponential(1 / exp_v3, N)
v4 = np.random.uniform(low_v4, high_v4, N)
# Проверка выполнения ограничений
constraints = (v1 + v2**2 >= 3) & (v3 + v4**2 <= 9)
probability = np.sum(constraints) / N
print(f"Вероятность выполнения ограничений: {probability}")