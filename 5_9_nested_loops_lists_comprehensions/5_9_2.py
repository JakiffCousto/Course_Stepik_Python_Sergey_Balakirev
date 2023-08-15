'''
Подвиг 2.
Вводится список целых чисел в строку через пробел.
С помощью list comprehension сформировать из них двумерный
список lst размером N x N (квадратную таблицу чисел).
Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу).
Результат отобразить в виде списка командой:
print(lst)
Sample Input:
1 2 3 4 5 6 7 8 9
Sample Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
# lst_in = list(map(int, input().split()))
lst_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = int(len(lst_in) ** 0.5)
lst_out = [lst_in[i*3:i*3+3] for i in range(N)]
A = [[lst_in[i+j*N] for i in range(N)] for j in range(N)]
print(lst_out)
print(A)
