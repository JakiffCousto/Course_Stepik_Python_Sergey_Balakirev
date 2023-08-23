'''
Подвиг 2.
Используя замыкания функций,
объявите внутреннюю функцию,
которая увеличивает значение своего аргумента
на некоторую величину n - параметр внешней функции с сигнатурой:
def counter_add(n): ...
Вызовите внешнюю функцию counter_add со значением
аргумента 2 и результат присвойте переменной cnt.
Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
k = int(input())
Выведите результат на экран.
Sample Input:
5
Sample Output:
7
'''


# put your python code here
def counter_add(n):
    def num_add(x):
        x = x + n
        return x

    return num_add


k = int(input())
cnt = counter_add(2)
print(cnt(k))

