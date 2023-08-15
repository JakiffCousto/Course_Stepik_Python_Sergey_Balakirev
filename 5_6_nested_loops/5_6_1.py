'''
Подвиг 1.
Вводится натуральное число N (то есть, положительное, целое).
Требуется создать двумерный (вложенный) список размером N x N элементов, состоящий из всех единиц, а затем,
в последний столбец записать пятерки.
Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.
P.S. Будьте внимательны в конце строк пробелов быть не должно!
Sample Input:
4
Sample Output:
1 1 1 5
1 1 1 5
1 1 1 5
1 1 1 5
'''

num = int(input())
lst_column = []
lst_row = []
for i in range(num):
    lst_column = []
    for j in range(num):
        lst_column.append(1)
    lst_column[num-1] = 5
    lst_row.append(lst_column)
for y in range(len(lst_row)):
    print(lst_row[y])
