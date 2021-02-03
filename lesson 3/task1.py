# -*- coding: utf-8 -*-
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a, b):
    """
    деление
    :int a:
    :int b:

    """
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        print('деление на 0')


num1 = int(input('Введи число a: '))
num2 = int(input('Введи число b: '))

division(num1, num2)
