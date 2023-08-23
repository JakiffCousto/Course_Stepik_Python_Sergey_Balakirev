'''
Подвиг 1.
Используя замыкания функций, определите вложенную функцию,
которая бы увеличивала значение переданного параметра на 5
и возвращала бы вычисленный результат.
При этом внешняя функция должна иметь следующую сигнатуру:
def counter_add(): ...
Вызовите функцию counter_add
и результат ее работы присвойте переменной с именем cnt.
Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
k = int(input())
Выведите результат на экран.
Sample Input:
7
Sample Output:
12
'''


def counter_add():
    def add_num(x):
        x = x + 5
        return x

    return add_num


# k = int(input())
cnt = counter_add()
print(cnt(10))