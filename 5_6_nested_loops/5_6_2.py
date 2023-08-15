'''
Подвиг 2.
Вводится список из URL-адресов (каждый с новой строки).
Требуется в них заменить все пробелы на символ дефиса (-).
Следует учесть, что может быть несколько подряд идущих пробелов.
Результат преобразования вывести на экран в виде строк из URL-адресов.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
Sample Output:
django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
'''

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_out = []
for i in range(len(lst_in)):
    while ' ' in lst_in[i]:
        lst_in[i] = lst_in[i].replace(' ', '-')
    while '--' in lst_in[i]:
        lst_in[i] = lst_in[i].replace('--', '-')
    print(lst_in[i])
