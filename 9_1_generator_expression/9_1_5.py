'''
Подвиг 7.
Используя символы малых букв латинского алфавита (строка ascii_lowercase):
from string import ascii_lowercase
запишите генератор, который бы возвращал все сочетания из двух букв латинского алфавита.
Выведите первые 50 сочетаний на экран в строку через пробел.
Например, первые семь начальных сочетаний имеют вид:
aa ab ac ad ae af ag
'''
from string import ascii_lowercase

i = 0
g = (x + y for x in ascii_lowercase for y in ascii_lowercase)
for element in g:
    print(element, end=' ')
    i += 1
    if i == 50:
        break

print(list(g))
