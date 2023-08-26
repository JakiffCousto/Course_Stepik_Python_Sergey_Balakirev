lst_test = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет",
            '5;Балакирев;1;Нет']

order = ["Имя", "Зачет", "Оценка", "Номер"]


def key_sort(x, y=None):
    if y is None:
        y = order
    i = y.index(x[0])
    return i


g = [i.split(';') for i in lst_test]
print(*g)
f = list(zip(*g))
print(f)
# s = sorted(*f, key=lambda x: order.index(x[0]))
s = sorted(f, key=key_sort)
print(s)
q = tuple(zip(*s))
print(q)
