# Задание 7

A = int(input("Введите координату A: "))
B = int(input("Введите координату B: "))
C = int(input("Введите координату C: "))

ac = abs(C - A)
bc = abs(C - B)

total = ac + bc

print("Длина отрезка AC =", ac)
print("Длина отрезка BC =", bc)
print("Сумма длин =", total)