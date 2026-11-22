# Задание 9

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

width = abs(x2 - x1)
height = abs(y2 - y1)

S = width * height
P = 2 * (width + height)

print("Площадь S =", S)
print("Периметр P =", P)