'''
Подвиг 3.
Имеется кортеж:
t = (3.4, -56.7)
Вводится последовательность целых чисел в одну строчку через пробел.
Необходимо их добавить в кортеж t. Результат вывести на экран командой:
print(t)
Sample Input:
8 11 -5 2
Sample Output:
(3.4, -56.7, 8, 11, -5, 2)
'''
lst_in = list(map(float, input().split()))
t = (3.4, -56.7)
t = t + tuple(lst_in)
print(t)
