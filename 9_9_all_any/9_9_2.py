'''
Подвиг 2.
Вводится строка вещественных чисел через пробел.
Необходимо определить, есть ли среди них хотя бы одно отрицательное.
Вывести True, если это так и False - в противном случае.
Задачу реализовать с использованием одной из функций: any или all.
Sample Input:
8.2 -11.0 20 3.4 -1.2
Sample Output:
True
'''


# put your python code here
lst_in = list(map(float, input().split()))
res = any(map(lambda x: x < 0, lst_in))
print(res)
