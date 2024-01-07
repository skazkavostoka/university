# здесь уже необходимо выбрать на основе входных данных оптимальную стратегию использования мощностей системы защиты сервера
# по типу задач (от легких до сложных), ai, bi - множители интервала для нормального распределения, g - количество генераций данных на основе исходных данных
# и заранее введенных ai, bi. Старался сделать код универсальным
#  here it is already necessary to choose on the basis of the input data the optimal strategy of using the server protection system capacities
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
