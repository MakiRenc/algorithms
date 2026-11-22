# Задание 3

print("Введите координаты точки A:")
xa = int(input("xa: "))
ya = int(input("ya: "))

print("Введите координаты точки B:")
xb = int(input("xb: "))
yb = int(input("yb: "))

print("Введите координаты точки C:")
xc = int(input("xc: "))
yc = int(input("yc: "))

dist_b_sq = (xb - xa) ** 2 + (yb - ya) ** 2
dist_c_sq = (xc - xa) ** 2 + (yc - ya) ** 2

if dist_b_sq < dist_c_sq:
    distance = dist_b_sq ** 0.5
    print("Ближе точка B. Расстояние =", distance)
elif dist_c_sq < dist_b_sq:
    distance = dist_c_sq ** 0.5
    print("Ближе точка C. Расстояние =", distance)
else:
    print("Точки B и C находятся на одинаковом расстоянии от A")