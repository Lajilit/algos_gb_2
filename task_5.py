"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят, и сколько между ними находится букв.
"""

letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')

start_alphabet_number = ord('a')
letter_1_num = ord(letter_1) - start_alphabet_number + 1
letter_2_num = ord(letter_2) - start_alphabet_number + 1
number_letters_between = letter_2_num - letter_1_num - 1

print(f'Буква "{letter_1}" стоит на {letter_1_num} месте алфавита.\n'
      f'Буква "{letter_2}" стоит на {letter_2_num} месте алфавита.\n'
      f'Количество букв между ними: {number_letters_between}')