# Вариант 10

# Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
# шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
# "кличка" и "порода".

class Animal:
    def __init__(self, vid, paw, color):
        self.vid = vid
        self.paw = paw
        self.color = color

    def __str__(self):
        return f'Вид: {self.vid}; Количество лап: {self.paw}; Цвет шерсти: {self.color}'


class Dog(Animal):
    def __init__(self, vid, paw, color, nickname, breed):
        super().__init__(vid, paw, color)
        self.nickname = nickname
        self.breed = breed

    def __str__(self):
        return f'Вид: {self.vid}; Количество лап: {self.paw}; Цвет шерсти: {self.color}; Кличка: {self.nickname}; Порода: {self.breed}'


ani = Animal('Кошка', '4', 'Черный')
sob = Dog('Собака', '4', 'Черный', 'Тоби', 'Доберман')
print(ani)
print(sob)




