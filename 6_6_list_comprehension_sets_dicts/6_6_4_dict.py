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
str_test = "И что сказать и что сказать и нечего и точка"
lst_in = str_test.lower().split()
s = set(lst_in)
d = dict.fromkeys(s)
for i in s:
    sum = 0
    for j in lst_in:
        if i == j:
            sum = sum + 1
    d[i] = sum
print(d)
