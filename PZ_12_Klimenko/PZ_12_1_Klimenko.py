# Вариант 10.
#
# 1.В последовательности на n целых чисел найти и вывести:
#     1. максимальный среди отрицательных
#     2. элементы кратные двум
#     3. их сумму
from random import randint

lst = [randint(-100, 100) for i in range(10)]
lstNeg = [i for i in lst if i < 0]
lst2 = [i for i in lst if i % 2 == 0]
print(lst)
print('1. максимальный среди отрицательны: ', max(lstNeg))
print('2. элементы кратные двум: ', lst2)
print('3. их суммa: ', sum(lst2))
