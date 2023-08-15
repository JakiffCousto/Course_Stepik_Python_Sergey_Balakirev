'''
Подвиг 1.
Вводится двумерный список в виде таблицы целых чисел (см. пример ниже).
С помощью list comprehension преобразовать двумерный список в одномерный так,
чтобы значения элементов шли в обратном порядке.
Результат отобразить в виде строки из чисел, записанных через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
1 2 3 4
5 6 7 8
9 8 7 6
5 4 3 2
Sample Output:
2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
'''
lst_in = [[1, 2, 0, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]]

lst_out = [x for row in lst_in for x in range(len(row), 0, -1)]

lst_new = []
c = []
for i in lst_in:
    for j in i:
        c.append(j)

e = []
for j in range(len(lst_in)-1, -1, -1):
    for i in range(len(lst_in[j])-1, -1, -1):
        e.append(lst_in[j][i])

f = [lst_in[j][i] for j in range(len(lst_in)-1, -1, -1) for i in range(len(lst_in[j])-1, -1, -1)]
g = [j for i in lst_in[::-1] for j in i[::-1]]

d = [j for i in lst_in for j in i]

print(lst_out)
print(c)
print(d)
print(g)
