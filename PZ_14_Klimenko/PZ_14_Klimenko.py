# Вариант 10

# В исходном текстовом файле(Dostoevsky.txt) найти все фамилии с инициалами
# (например, А. Ф. Куманиной и т.п.)

import re
f1 = open("Dostoevsky.txt", encoding="UTF-8")
text = f1.read()
f1.close()
regex = re.compile(r"[А-ЯЁ]\.\s[А-ЯЁ]\.\s[А-ЯЁ][а-яё]+")
print(regex.findall(text))