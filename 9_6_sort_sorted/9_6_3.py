"""
Подвиг 4.
На вход программы поступает список целых чисел,
записанных в одну строчку через пробел. Необходимо выбрать
из них четыре наибольших уникальных значения.
Результат вывести на экран в порядке их убывания в одну строчку через пробел.
Sample Input:
10 5 4 -3 2 0 5 10 3
======================
Sample Output:
10 5 4 3
"""

s_test = '10 5 4 -3 2 0 5 10 3'
lst = list(map(int, s_test.split()))
f = set(lst)
g = sorted(f, reverse=True)
res = []
for i in range(4):
    res.append(g[i])
print(*res)
