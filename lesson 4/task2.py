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

#new_list3 = [i + x for i, x in (new_list, new_list2)]
#new_list = [el for el in test if el > ]
#[x**2 if x%2 else x for x in xrange(100)]
##new_list = [el if el else x for el in test]
#new_list = [test[i] for i in range(len(test)) if (test[i] > test[i + 1])]
#new_list = [test[i] for i in range(len(test)) lam if (test[i] > test[i + 1])]

#list_d = [(i, x) for i, x in enumerate(list_a)]
#list_e = [x for i, x in enumerate(list_a, 1) if i % 3 == 0]



'''
new_list = []
for i in range(0, len(test), 2):
    print(i, el)
    if test[i] > c + 1]:
        new_list.append(test[i])
    else:
        new_list.append(test[i+ i)

'''

print(new_list)
print(new_list2)
print(new_list3)





