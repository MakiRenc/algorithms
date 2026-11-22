# Задание 6

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

dx = x2 - x1
dy = y2 - y1

distance = (dx ** 2 + dy ** 2) ** 0.5

print("Расстояние =", distance)