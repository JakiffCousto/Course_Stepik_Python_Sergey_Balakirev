'''
Подвиг 2.
Вводится неравномерная таблица целых чисел.
С помощью функции zip выровнить эту таблицу,
приведя ее к прямоугольному виду, отбросив выходящие элементы.
Вывести результат на экран в виде такой же таблицы чисел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
1 2 3 4 5 6
3 4 5 6
7 8 9
9 7 5 3 2
Sample Output:
1 2 3
3 4 5
7 8 9
9 7 5
'''


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
f = list(x.split() for x in lst_in)
print(f)
z = zip(*f)
lz = zip(*z)
for x in lz:
    print(*x)