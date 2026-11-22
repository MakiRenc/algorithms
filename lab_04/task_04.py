# Задание 4

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

text = input("Введите строку: ")
if is_palindrome(text):
    print("Это палиндром")
else:
    print("Это не палиндром")