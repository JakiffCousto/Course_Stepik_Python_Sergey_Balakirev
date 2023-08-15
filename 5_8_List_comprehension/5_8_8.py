'''
Подвиг 8.
Вводятся два списка целых чисел одинаковой длины каждый с новой строки.
С помощью list comprehension сформировать третий список,
состоящий из суммы соответствующих пар чисел введенных списков.
Результат вывести на экран в одну строку через пробел.
Sample Input:
1 2 3 4 5
6 7 8 9 10
Sample Output:
7 9 11 13 15
'''
lst_first = list(map(int, input().split()))
lst_second = list(map(int, input().split()))
lst_out = [lst_first[i] + lst_second[i] for i in range(len(lst_first))]
print(*lst_out)
