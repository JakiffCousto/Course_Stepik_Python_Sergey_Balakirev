'''
Подвиг 2. Вводятся два целых положительных числа n и m, причем, n < m.
Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m].
Программу реализовать при помощи цикла while.
Sample Input:
2 4
Sample Output:
4 9 16
'''

# put your python code here
n, m = map(int, input().split())
i = n

while i <= m:
    print(i ** 2, end=' ')
    i = i + 1

