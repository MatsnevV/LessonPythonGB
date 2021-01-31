# -*- coding: utf-8 -*-
"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(my_str):
    if my_str:
        return my_str[0].upper() + my_str[1:]
    return my_str


def int_func_strora(my_str):
    ls = my_str.split()
    for i, j in enumerate(ls):
        ls[i] = int_func(j)
    return ' '.join(ls)


print(int_func_strora(input('Введите слво или предложение.\n>')))