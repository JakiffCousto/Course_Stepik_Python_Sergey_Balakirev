'''
Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
Далее, на вход программы поступают две строки: первая - это значение для параметра tp;
вторая - список целых чисел, записанных через пробел.
С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
Результат вывести на экран командой (lst - ссылка на коллекцию):

print(lst)
'''

s = '-5 6 8 11 0 111 -456 3'
lst_t = list(map(int, s.split()))
t_t = tuple(map(int, s.split()))
print("lst:", lst_t)
print("tuple:", t_t)


def outer(tp):
    def inner(s):
        nonlocal tp
        if tp == "list":
            x = list(map(int, s.split()))
        else:
            x = tuple(map(int, s.split()))
        return x

    return inner


t = input()
s = input()
f = outer(t)
print(f(s))