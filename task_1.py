"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

user_number = int(input('Введите трехзначное целое число: '))

n1 = user_number // 100
n2 = user_number // 10 % 10
n3 = user_number % 10

print(n1 + n2 + n3)
print(n1 * n2 * n3)
