'''
Подвиг 1.
На вход поступает список из вещественных чисел,
записанных в строку через пробел.
С помощью функции map преобразовать числа в строке в их вещественное
представление и отобразить первые три числа.
(Полагается, что минимум три вещественных числа имеются).
Реализовать извлечение чисел через функцию next.
Результат отобразить в строку через пробел.
Sample Input:
4.35 -10.6 1.0 200.34 0.56
Sample Output:
4.35 -10.6 1.0
'''


a = map(float, input().split())
print(next(a), end=' ')
print(next(a),  end=' ')
print(next(a),  end=' ')