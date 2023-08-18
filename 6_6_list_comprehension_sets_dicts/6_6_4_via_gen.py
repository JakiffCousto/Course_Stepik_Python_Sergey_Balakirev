'''
Подвиг 5.
Вводится текст в одну строчку со словами через пробел.
Используя генераторы множеств и словарей, сформировать словарь в формате:
{слово_1: количество_1, слово_2: количество_2, ..., слово_N: количество_N}
То есть, ключами выступают уникальные слова (без учета регистра),
а значениями - число их встречаемости в тексте. На экран вывести значение словаря для слова (союза) 'и'.
Если такого ключа нет, то вывести 0.
Sample Input:
И что сказать и что сказать и нечего и точка
Sample Output:
4
'''

str_test = " что сказать что сказать нечего точка"
lst_in = str_test.lower().split()
d = {x: lst_in.count(x) for x in {y for y in lst_in}}
print(0 if 'и' not in d else d['и'])
