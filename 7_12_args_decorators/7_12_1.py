'''
Подвиг 1.
Вводится строка целых чисел через пробел.
Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.
Sample Input:
5 6 3 6 -4 6 -1
Sample Output:
26
'''


# put your python code here
def func_decorator(start=5):
    def decorator(func):
        def inner(*args):
            return start + func(*args)

        return inner

    return decorator


@func_decorator(start=5)
def f_sum(s: str):
    lst = list(map(int, s.split()))
    sum_num = sum(lst)
    return sum_num


s_input = input()
print(f_sum(s_input))
