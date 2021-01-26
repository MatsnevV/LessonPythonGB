# -*- coding: utf-8 -*-
""""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

num_a = int(input(f'Введи число a: '))
num_b = int(input(f'Введи число b: '))
num_c = int(input(f'Введи число c: '))


def my_func(a, b, c):
    """
    сравнение трех чисел  и суммирование наибольших из них
    """
    num1 = a if a > b else b
    num2 = b if b > c else c
    return num1 + num2


print(my_func(num_a, num_b, num_c))
