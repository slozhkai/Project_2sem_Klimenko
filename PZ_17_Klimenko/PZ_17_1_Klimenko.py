# Вариант 10

# Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите
# метод, который выводит информацию о здании в формате "Адрес: адрес, Количество
# этажей: этажи".

class Building:
    def __init__(self, adress, floors):
        self.adress = adress
        self.floors = floors

    def display_info(self):
        print(f'Адрес: {self.adress}, Количество этажей: {self.floors}')


first = Building('2-я Краснодарская 80/3', '15')
second = Building('пр. Коммунистический 155', '10')
first.display_info()
second.display_info()


