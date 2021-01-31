# -*- coding: utf-8 -*-
"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

num_a = int(input('Введи первое значение\n >'))
num_b = int(input('Введи второе значение (оно должно быть отрицательным)\n >'))


def my_func(x, y):
    """
    возведение в степень через **
    """
    return x ** y


def my_func_two(x, y):
    """
        возведение в степень через цикл
    """
    z = x
    y = y if y > 0 else -y
    for i in range(y - 1):
        z = z * x
    return 1 / z


print(my_func(num_a, num_b))
print(my_func_two(num_a, num_b))