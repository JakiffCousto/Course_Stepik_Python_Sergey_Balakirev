'''
Подвиг 3.
На вход функции с именем get_sort поступает словарь, например, такой:
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
Необходимо отсортировать словарь d по убыванию ключей (лексикографическая сортировка строк) и возвратить список из соответствующих значений ключей словаря. Например, для указанного словаря d, результатом должен быть список:
['дерево', 'лошадь', 'собака', 'кот', 'книга']
Сигнатура функции get_sort должна быть следующей:
def get_sort(d): ...
В программе только определить функцию, вызывать ее не нужно и что-либо выводить на экран тоже не нужно.
P. S. Подсказка: список в функции get_sort лучше всего формировать с помощью генератора списков.

Sample Input:
Sample Output:
True
'''
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}


def get_sort(x):
    y = sorted(x.items(), reverse=True)
    lst = []
    for i in y:
        lst.append(i[1])
    return lst


print(get_sort(d))