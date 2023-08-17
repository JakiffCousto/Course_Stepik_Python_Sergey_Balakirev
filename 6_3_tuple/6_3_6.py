'''
Подвиг 8.
Вводятся целые числа в одну строку через пробел.
На их основе формируется кортеж.
Необходимо найти и вывести все индексы неуникальных (повторяющихся) значений в этом кортеже.
Результат отобразите в виде строки чисел, записанных через пробел.
Sample Input:
5 4 -3 2 4 5 10 11
Sample Output:
0 1 4 5
'''
t_in = tuple(map(int, input().split()))
lst_index = []
for i in range(len(t_in)):
    for j in range(len(t_in)):
        if t_in[i] == t_in[j] and i !=j and i not in lst_index:
            lst_index.append(i)
print(*lst_index)