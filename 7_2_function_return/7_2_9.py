'''
Подвиг 9.
Вводится список целых чисел в одну строчку через пробел.
Необходимо задать функцию, которая принимает два аргумента
(максимальное и минимальное значения из списка) и возвращает их произведение.
Вызовите эту функцию и отобразите на экране полученное числовое значение.
Подсказка: для передачи аргументов функции используйте функции max и min для введенного списка чисел.
Sample Input:
56 34 -30 22 1 4 10
Sample Output:
-1680
'''
def get_cal(x, y):
    return x * y


lst_in = list(map(int, input().split()))
a = max(lst_in)
b = min(lst_in)
print(get_cal(a, b))
