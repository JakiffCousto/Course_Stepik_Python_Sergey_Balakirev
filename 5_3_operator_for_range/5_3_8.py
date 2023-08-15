'''
Подвиг 8.
Вводится натуральное число n.
С помощью цикла for определить, является ли оно простым (то есть, делится нацело только на само себя и на 1).
Вывести на экран ДА, если n простое и НЕТ - в противном случае.
Sample Input:
11
Sample Output:
ДА
'''
# put your python code here
n = int(input())
key = False
for i in range(2, n, 1):
    if n % i == 0:
        key = True
if key:
    print('НЕТ')
else:
    print('ДА')
