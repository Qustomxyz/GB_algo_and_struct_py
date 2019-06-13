"""
Задача 5.
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

letter1 = input('Введите первую букву: ')
letter2 = input('Введите вторую букву: ')

shift = ord('a') - 1
letter1_order = ord(letter1) - shift
letter2_order = ord(letter2) - shift
letters_amount = abs(letter1_order - letter2_order) - 1

# вариант одинаковых букв не рассматриваем следуюя концепции "идеального пользователя"

print(f"Буква '{letter1}' в алфавите имеет порядковый номер {letter1_order}.")
print(f"Буква '{letter2}' в алфавите имеет порядковый номер {letter2_order}.")
print(f"Количество букв между '{letter1}' и '{letter2}': {letters_amount}.")