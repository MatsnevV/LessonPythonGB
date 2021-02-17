"""
 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
 Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
 Выполнить подсчет средней величины дохода сотрудников.
"""


def sred_znach(my_list):
    k = 0
    for i in my_list:
        k += float(i[1])
    return k / len(my_list)


def min_znach(znach):
    print(f'Сотрудник с зарплатой меньше 20к :')
    for i in znach:
        if float(i[1]) < 20000:
            print(f'\t\t\t\t\t\t\t\t\t{i[0]}:  {i[1]}')


my_f = open("text_task3.txt", "r")
content = my_f.read()
g = [el.split(" ") for el in content.split("\n")]
print(f'Cреднее значение зарплатной платы по всем сотрудникам: {sred_znach(g)}')
min_znach(g)
my_f.close()
