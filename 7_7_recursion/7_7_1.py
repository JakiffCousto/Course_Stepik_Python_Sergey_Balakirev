'''
7.7 Рекурсивные функции
Подвиг 2.
Вводится целое положительное число N.
Необходимо написать рекурсивную функцию с именем get_rec_N,
которая отображает на экране последовательность целых чисел от 1 до N (включительно).
Каждое число выводится с новой строки.
В качестве параметра функция get_rec_N должна
принимать одно числовое значение. То есть, иметь только один параметр.
Начальный вызов функции будет выглядеть так:
get_rec_N(N)
Вызывать функцию не нужно, только объявить.
Sample Input:
8
Sample Output:
1
2
3
4
5
6
7
8
'''

# считывание числа N
N = int(input())


# здесь продолжайте программу
def get_rec_N(N):
    if N > 0:
        get_rec_N(N - 1)
        print(N)
