# Вариант 10.
# 2. Из заданной строки отобразить только цифры. Использовать библиотеку string.
# Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
# 481 feet (147 metres) high.
from string import digits
st = 'TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high.'
lst = [i for i in st if i in digits]
print('Цифры: ',  ' '.join(lst))
