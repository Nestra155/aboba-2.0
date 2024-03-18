'''
Напишите программу, которая принимает символ (т.е. строку длины 1) и возвращает True, если это гласная, в противном случае False.

Sample Input 1:
a

Sample Output 1:
True

Sample Input 2:
b
'''
# Запрос ввода символа от пользователя
char = input("Введите символ: ")

# Проверка символа на гласность
vowels = "aeiouAEIOU"
if char in vowels:
    print(True)
else:
    print(False)
