'''
Подвиг 2.
Имеется одномерный список длиной 10 элементов, состоящий из нулей:
p = [0] * 10
На каждой итерации цикла пользователь вводит целое число - индекс элемента списка p, по которому записывается значение 1,
если ее там еще нет. Если же 1 уже проставлена, то список не менять и снова запросить у пользователя очередное число.
Необходимо расставить так пять единиц в список. (После этого цикл прерывается).
Программу реализовать с помощью цикла while и с использованием оператора continue,
когда 1 не может быть добавлена в список. Результат вывести на экран в виде последовательности чисел, записанных через пробел.
Sample Input:
1
2
2
5
7
5
9
Sample Output:
0 1 1 0 0 1 0 1 0 1
'''
# put your python code here
p = [0] * 10
sum_p = 0
while sum_p < 5:
    i = int(input())
    if p[i] == 1:
        continue
    else:
        p[i] = 1
        sum_p = sum_p + 1
print(*p)
