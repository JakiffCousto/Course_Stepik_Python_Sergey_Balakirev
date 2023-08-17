'''
Подвиг 6.
Вводятся данные в формате:
<день рождения 1> имя_1
<день рождения 2> имя_2
...
<день рождения N> имя_N
Дни рождений и имена могут повторяться.
На их основе сформировать словарь и вывести его в формате (см. пример ниже):
день рождения 1: имя1, ..., имяN1
день рождения 2: имя1, ..., имяN2
...
день рождения M: имя1, ..., имяNM
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана
Sample Output:
3: Сергей
5: Николай, Юлия
4: Елена, Светлана
7: Владимир
'''
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
B = [lst_in[i].split() for i in range(len(lst_in))]
F = []
for i in lst_in:
    row = i.split()
    F.append(row[0])
d = dict.fromkeys(F)
print(d)
d_key = list(d)
for i in range(len(d)):
    C = []
    for j in range(len(B)):
        if d_key[i] == B[j][0]:
            C.append(B[j][1])
    d[d_key[i]] = C
for key, value in d.items():
    print(key, ", ".join(value), sep=':')

# for key, value in d.items():
#     value_string = ''
#     for x in value:
#         value_string = value_string + ", " + x
#     print(key, value_string, sep=':')