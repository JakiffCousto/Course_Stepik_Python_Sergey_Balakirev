'''
Подвиг 3.
Вводится таблица целых чисел.
Используя функцию map и генератор списков,
преобразуйте список строк lst_in (см. листинг)
в двумерный список с именем lst2D, содержащий целые числа.
Выводить на экран ничего не нужно,
только сформировать список lst2D на основе введенных данных.
Sample Input:
8 11 -5
3 4 10
-1 -2 3
4 5 6
Sample Output:
True
'''




import sys
test_str = "8 11 -5" \
           "3 4 10" \
           "-1 -2 3" \
           "4 5 6"
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = map(str.split, lst_in)
print(lst_in)
print(lst2D)

lst_test = []
for x in lst2D:
    lst_temp = []
    for y in x:
        lst_temp.append(int(y))
    lst_test.append(lst_temp)
print(lst_test)

g = [list(int(y) for y in x) for x in map(str.split,lst_in)]
g_2 = [list(map(int, x.split())) for x in lst_in]
print(g)
