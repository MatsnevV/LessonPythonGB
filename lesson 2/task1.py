# -*- coding: utf-8 -*-
""" Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

tip_fset = frozenset('1')
tip_set = set('1')
tip_tuple = tuple('1')
tip_dict = dict(x='1')
tip_int = 1
tip_str = '1'
tip_float = 1.0
tip_none = None
tip_list = list('1')
tip_complex = complex(1, 2)
tip_bin = bin(1)

ls = [tip_fset, tip_set, tip_tuple, tip_dict, tip_int, tip_str,tip_float, tip_none, tip_list, tip_complex, tip_bin, ]

for i in ls:
    print(f'Значение: {i} , тип занчения: {type(i)}')







