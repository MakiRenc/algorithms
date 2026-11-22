# Задание 5

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

my_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_num = int(input("Введите число для поиска: "))

result = binary_search(my_list, target_num, 0, len(my_list) - 1)

if result != -1:
    print("Элемент найден на индексе:", result)
else:
    print("Элемент не найден")