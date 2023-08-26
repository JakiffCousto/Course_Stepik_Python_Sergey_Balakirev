'''
Значимый подвиг 4.
Имеется таблица с данными, представленная в формате:
Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
...
N;Балакирев;4;Да

Эти данные необходимо представить в виде двумерного (вложенного) кортежа.
Все числа должны быть представлены как целые числа. Затем, отсортировать данные так,
чтобы столбцы шли в порядке:

Имя;Зачет;Оценка;Номер

Реализовать эту операцию с помощью сортировки.
Результат должен быть представлен также в виде двумерного кортежа и присвоен переменной с именем t_sorted.
Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
Номер;Имя;Оценка;Зачет
1;Портос;5;Да
2;Арамис;3;Да
3;Атос;4;Да
4;д'Артаньян;2;Нет
5;Балакирев;1;Нет
Sample Output:
True
'''
import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_test = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет",
            '5;Балакирев;1;Нет']
g = [i.split(';') for i in lst_test]
numbers = [str(i) for i in range(10)]
t_sorted = ()
for i in range(len(g)):
    temp = ()
    for j in range(len(g[i])):
        temp = g[i][0]
        g[i][0] = g[i][1]
        g[i][1] = g[i][3]
        g[i][3] = temp
        if g[i][j] in numbers:
            g[i][j] = int(g[i][j])
    print(g[1][2])
    print(type(g[1][2]))
    f = tuple(g[i],)
    t_sorted = t_sorted + (f,)

print(t_sorted)

#There is 2nd option:
# здесь продолжайте программу (используйте список строк lst_in)
order = "Имя;Зачет;Оценка;Номер"
t = tuple(tuple(int(st) if st.isdigit() else st for st in row.split(";")) for row in lst_test)
t_sorted = tuple(zip(*sorted(list(zip(*t)), key=lambda x: order.find(x[0]))))

#There is 3rd option:
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