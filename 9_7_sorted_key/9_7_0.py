'''
Подвиг 1.
На вход программы поступает список наименований рек,
записанных в одну строчку через пробел.
Необходимо отсортировать этот список в порядке убывания длин названий.
Результат вывести в одну строчку через пробел.
Sample Input:
Лена Енисей Волга Дон
Sample Output:
Енисей Волга Лена Дон
'''


def id_odd(x):
    return x % 2


def key_sort(x):
    return x if x % 2 == 0 else 100 + x


a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=id_odd)
print(b)
c = sorted(a, key=lambda x: x % 2)
print(c)
d = a
d.sort(key=lambda x: x % 2)
print(d)

e = sorted(a, key=key_sort)
print(e)

lst = ['Moscow', 'Tver', 'Smolensk', 'Pskov', 'Ryazan']

f = sorted(lst, key=len)
print(f)
g = sorted(lst, key=lambda x: x[-1])
print(g)

books = (
    ('Evgeniy Onegin', 'Pushkin AC', 200),
    ('Mumu', 'Turgenev IC', 250),
    ('Master and Margo', 'Bulgakov MA', 500),
    ('Dead souls', 'Gogol', 190)
)

h = sorted(books, key=lambda x: x[-1])
print(h)
print(type(books[0]))