"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


test = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res_test = [12, 44, 4, 10, 78, 123]


new_list = [el for i, el in enumerate(test, 1) if i % 2 == 0]
new_list2 = [el for i, el in enumerate(test, 1) if i % 2 != 0]
new_list3 = [[i if i > j else j for i in new_list]for j in new_list2]
test2 =[]
for i in range(0, len(new_list2)):
    if new_list[i] > new_list2[i]:
        test2.append(new_list[i])
    else:
        test2.append(new_list2[i])


print(new_list)
print(new_list2)
print(new_list3)





