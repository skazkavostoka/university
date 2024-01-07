import numpy as np

def reshenie(x, a=0.2, b=0.2):
    x1 = x - (x*a)
    x2 = x + (x*b)
    average = (x1 + x2) / 2
    # Среднее значение интервала
    standart_deviation = (x2 - x1) / 4
    # Стандартное отклонение по формуле (b-a) / 4
    random_sign = np.random.normal(average, standart_deviation)
    # Генерируем случайное значение
    return random_sign
ai, bi = float(input('Введите ai: ')), float(input('Введите bi: '))
g = int(input('Введите количество генераций: '))
ishod = [int(input("введите следующее ограничение: ")) for i in range(4)]
vihod = [[0 for i in range(4)] for j in range(2)]
#сгенерируем исходный список
#и вложенные результирующие списки, изначально заполненные нулями
for i in range(g):
    for j in range(len(vihod[i])):
        vihod[i][j] = int(reshenie(ishod[j], ai, bi))
print(vihod)