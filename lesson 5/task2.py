"""
Создать текстовый файл (не программно), 
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""


def counters(args):
    for i, j in enumerate(args, 1):
        flag = False
        slov_in_str = 0
        for k in j:
            if not flag and k != ' ':
                slov_in_str += 1
                flag = True
            elif flag and k == ' ':
                flag = False
        print(f'{i})строка {slov_in_str} слов.')


my_f = open("text_task2.txt", "r")
content = my_f.read()
count_str = content.count('\n') + 1
print(f'Колличество строк составило: {count_str}')
counters(content.split("\n"))
my_f.close()
