# Вариант 10

# В матрице найти среднее арифметическое положительных элементов.

import numpy as np

lst = np.array([[4, -52, -1, 7], [2, -16, 5, 21], [8, 7, -98, 14]], int)
print('Матрица:\n', lst)

res = [x for y in lst for x in y]
res = list(filter(lambda x: x > 0, res))
print('Положительные элементы матрицы:\n', res)

a = sum(res) / len(res)
print('Среднее арифметическое положительных элементов матрицы:\n', a)
