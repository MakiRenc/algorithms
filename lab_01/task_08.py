# Задание 8

A = int(input("Введите координату A: "))
B = int(input("Введите координату B: "))
C = int(input("Введите координату C (между A и B): "))

ac = abs(C - A)
bc = abs(B - C)

product = ac * bc

print("Длина отрезка AC =", ac)
print("Длина отрезка BC =", bc)
print("Произведение длин AC и BC =", product)