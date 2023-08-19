'''
Подвиг 5.
Объявите функцию для проверки числа на нечетность
(возвращается True, если переданное число нечетное и False, если число четное).
После объявления функции прочитайте (с помощью функции input)
список целых значений, записанных в одну строку через пробел.
И, используя генератор списков и созданную функцию,
сформируйте список из нечетных значений на основе введенного исходного списка.
Результат отобразите на экране командой:
print(*lst)
где lst - сформированный список из нечетных значений.
Sample Input:
8 11 -15 3 2 10
Sample Output:
11 -15 3
'''
def get_not_even(x):
    return x % 2 != 0


lst_in = list(map(int, input().split()))
lst_not_even = [y for y in lst_in if get_not_even(y) == True]
print(*lst_not_even)