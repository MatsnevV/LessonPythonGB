"""
 Создать программно файл в текстовом формате, 
 записать в него построчно данные, вводимые пользователем.
  Об окончании ввода данных свидетельствует пустая строка.
"""


print('Введите текст')
with open("text_task1.txt", "w") as f_obj:
    while True:
        znach_in = input(">")
        print(znach_in, file=f_obj)
        if znach_in in "\n":
            break
