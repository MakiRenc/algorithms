# Задание 10

year = int(input("Введите год: "))

diff = year - 1984

color_index = (diff // 2) % 5
animal_index = diff % 12

colors = ["зеленый", "красный", "желтый", "белый", "черный"]
animals = [
    "крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
    "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"
]

print("Год", colors[color_index] + " " + animals[animal_index])