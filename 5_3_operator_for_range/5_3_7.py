'''
Подвиг 7.
Вводится натуральное число n.
С помощью цикла for найти все делители этого числа.
Найденные делители выводить сразу в столбик без формирования списка.
Sample Input:
12
Sample Output:
1
2
3
4
6
12
'''
# put your python code here
n = int(input())
for i in range(1,n+1,1):
    if n % i == 0:
        print(i)
