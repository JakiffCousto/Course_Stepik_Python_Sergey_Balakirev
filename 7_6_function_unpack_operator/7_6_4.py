'''
Подвиг 5.
Вводится список вещественных чисел и список названий городов,
каждый в отдельной строке. Необходимо сформировать единый
список lst, в котором сначала идут числа, а затем, названия городов.
Реализовать программу с помощью оператор распаковки *.
Вывести полученный список на экран командой:
print(*lst)
Sample Input:
5.8 11.0 4.3
Уфа Омск Тверь Самара
Sample Output:
5.8 11.0 4.3 Уфа Омск Тверь Самара
'''

import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

my_dick = {}
for i in lst_in:
    index, value = i.split('=')
    my_dick[index] = value
menu = {**menu, **my_dick}
print(menu)