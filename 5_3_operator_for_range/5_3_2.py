'''
Подвиг 2.
С помощью функции range() сформируйте следующую последовательность чисел:
10, 9, 8, ..., 0
Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.
Sample Input:
Sample Output:
10 9 8 7 6 5 4 3 2 1 0
'''
# put your python code here
for i in range(10, -1, -1):
    print(i, end=" ")
