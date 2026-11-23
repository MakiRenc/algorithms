# Бинарный поиск

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1
            
        else:
            left = mid + 1
            
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print("Отсортированный массив:", arr)
target = int(input("Введите число для поиска: "))

result = binary_search(arr, target)

if result != -1:
    print("Элемент найден на индексе:", result)
else:
    print("Элемент не найден")