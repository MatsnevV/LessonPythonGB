"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_f = open("text_task5.txt", "w")
stroka = input('Введите ряд чисел через пробел " "\n>')
content_out = my_f.write(stroka)
my_f.close()

try:
    my_f = open("text_task5.txt", "r")
    content_in = my_f.read()
    count_str = sum(map(int, content_in.split(" ")))
    print(f'Сумма составила: {count_str}')
except IOError:
    print("Произошла ошибка ввода-вывода!")
except ValueError:
    print('Введен пробе в конце .не допустимо!')
finally:
    my_f.close()