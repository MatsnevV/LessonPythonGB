# -*- coding: utf-8 -*-
"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""

stroka_in = input()
stroka_list = list(stroka_in)
res = []

for i in range(0, len(stroka_in) - 1, 2):
    res.append(stroka_list[i + 1])
    res.append(stroka_list[i])

if (len(stroka_in) % 2) != 0:
    res.append(stroka_in[-1])

print(res)
