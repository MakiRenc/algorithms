# Задание 1

price = float(input("Введите цену 1 кг конфет: "))

for i in range(1, 11):
    weight = i / 10
    cost = price * weight
    print("Стоимость", weight, "кг =", cost)