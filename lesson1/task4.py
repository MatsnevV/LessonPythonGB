# -*- coding: utf-8 -*-
"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
n = input('Введите целое положительное число: ')
ls = list(map(int, n))
k = 0
for i in ls:
    if i > k:
        k = i
print(k)
