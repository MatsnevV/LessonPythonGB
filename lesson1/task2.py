# -*- coding: utf-8 -*-
"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
sec_time_in = int(input('Введи время в секундах: '))

chas_time_out = sec_time_in // 3600
min_time_out = (sec_time_in // 60) - (chas_time_out * 60)
sec_time_out = sec_time_in % 60

print(f'{chas_time_out:02}:{min_time_out:02}:{sec_time_out:02}')

