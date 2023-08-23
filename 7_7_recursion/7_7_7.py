'''
7.7 Рекурсивные функции
Задача 7
Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел.
Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка и отобразите результат
на экран в виде последовательности чисел, записанных через пробел.
Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
'''


def mass_sep(lst_input, a = []):
    if len(lst_input) < 2:
        return lst_input
    else:
        mass_sep(lst_input[:int(len(lst_input)/2)])
        mass_sep(lst_input[int(len(lst_input) / 2):])
        return lst_input[0]


def fun(lst_input, lst=None):
    if lst is None:
        lst = []
    if len(mass_sep(lst_input)) == 1 and mass_sep(lst_input) > 0:
        lst.append(mass_sep(lst_input))
        return lst

lst_test = [8, 11, -6, 3, 0, 1, 1]
print(mass_sep(lst_test))
# print(fun(lst_test))