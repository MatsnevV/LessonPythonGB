"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
           }

with open("text_task4.txt") as f_obj:
    with open("text_task4_new.txt", "w") as g_obj:
        for i in f_obj:
            k = i.split(' ')
            g = k[2]
            h = my_dict[int(g[0])]
            print(f'{h} - {g}', file=g_obj, end='')