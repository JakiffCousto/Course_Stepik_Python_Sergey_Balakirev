'''
Подвиг 5.
Вводится строка.
Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
(символ, порядковый индекс)
Первый индекс имеет значение 0.
Строка может быть короче 10 символов, а может быть и длиннее.
То есть, число пар может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.
Программа ничего не должна отображать на экране, только формировать список из кортежей.
================
Sample Input:
Python дай мне силы пройти этот курс до конца!
================
Sample Output:
True
'''
s = 'Python дай мне силы пройти этот курс до конца!'
c = tuple(x for x in s[0:10])
f = tuple(s.index(x) for x in s)


z = zip(c, f)

for i in z:
    print(i)