'''
Подвиг 8.
В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
Вводится натуральное число n.
Как наименьшим количеством таких денежных купюр можно выплатить сумму n?
Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей).
Предполагается, что имеется достаточно большое количество купюр всех достоинств.
Sample Input:
221
Sample Output:
64 64 64 16 8 4 1
'''

import math

n = int(input())
lst_money = [64, 32, 16, 8, 4, 2, 1]
lst_qty = []
lst_q = []
i = 0
key = False
while not key:
    q = int(math.floor(n / lst_money[i]))
    r = n % lst_money[i]
    n = n - q * lst_money[i]
    if r == 0:
        key = True
    for j in range(int(q)):
        print(lst_money[i], end=' ')
    i = i + 1