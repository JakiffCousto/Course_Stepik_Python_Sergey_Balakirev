'''
Подвиг 3.
Вводится натуральное число n.
Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне [2; n).
Результат вывести на экран в строчку через пробел.
Sample Input:
11
Sample Output:
2 3 5 7
'''
num_in = int(input())
for i in range(2, num_in):
    key = False
    for j in range(2, i-1):
        if i % j == 0:
            key = True
            break
    if not key:
        print(i, end=' ')



