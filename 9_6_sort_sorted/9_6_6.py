'''
Подвиг 6.
На вход программы поступает список товаров в формате:
название_1:цена_1
...
название_N:цена_N
Необходимо преобразовать этот список в словарь,
ключами которого выступают цены (целые числа),
а значениями - соответствующие названия товаров.
Необходимо написать функцию, которая бы принимала на входе
словарь и возвращала список из наименований трех наиболее дешевых товаров.
Вызовите эту функцию и отобразите на экране полученный список в порядке
возрастания цены в одну строчку через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
смартфон:120000
яблоко:2
сумка:560
брюки:2500
линейка:10
бумага:500
Sample Output:
яблоко линейка бумага
'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
d = {int(x.split(':')[1]): x.split(':')[0] for x in lst_in}


def get_sort(x):
    y = sorted(x.items())
    lst = []
    for i in range(3):
        lst.append(y[i][1])
    return lst


print(*get_sort(d))
