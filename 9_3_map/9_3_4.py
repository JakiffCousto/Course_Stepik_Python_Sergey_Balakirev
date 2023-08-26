'''
Подвиг 4.
На вход программы поступает строка в формате:
ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
Sample Input:
house=дом car=машина men=человек tree=дерево
Sample Output:
True
'''


# ввод строки (переменную s не менять)
# s = input()
s_test = "house=дом car=машина men=человек tree=дерево"
s_lst = s_test.split()


t = tuple(tuple(map(str, x.split('='))) for x in s_lst)
s = tuple(map(tuple,[x.split('=') for x in s_lst]))
tp = tuple(map(tuple, (i.split('=') for i in s_lst)))
print(t)
print(s)
print(tp)
# здесь продолжайте программу