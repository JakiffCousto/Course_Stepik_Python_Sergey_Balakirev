'''
Подвиг 5.
Вводится строка, содержащая латинские символы,
пробелы и цифры. Необходимо выделить из нее все неповторяющиеся цифры
(символы от 0 до 9) и вывести на экран в одну строку через пробел их в
порядке возрастания значений. Если цифры отсутствуют, то вывести слово НЕТ.
Sample Input:
Python 3.9.11 - best language!
Sample Output:
1 3 9
'''
str_test = 'Python - best language!'
s = set()
for v in str_test:
    if v.isdigit():
        s.add(v)

if len(s) > 0:
    print(*sorted(s))
else:
    print('НЕТ')
