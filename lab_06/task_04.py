# Задание 4

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

result = []
left = 0
right = N - 1

while left <= right:
    result.append(arr[left])
    left += 1
    
    if left <= right:
        result.append(arr[right])
        right -= 1

print("Результат:", result)