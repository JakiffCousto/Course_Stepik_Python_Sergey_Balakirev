'''
Подвиг 7.
Вводится натуральное (то есть, целое положительное) число (от трехзначного и более).
Найти произведение всех его цифр. Результат вывести на экран. Программу реализовать при помощи цикла while.
Sample Input:
821
Sample Output:
16
'''

# put your python code here
a = input()
lst = list(map(int, a))
i = 0
ml = 1
while i < len(lst):
    ml = ml * lst[i]
    i = i + 1
print(ml)


