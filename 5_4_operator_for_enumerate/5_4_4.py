'''
Подвиг 4.
Вводится список в виде целых чисел в одну строку через пробел.
Необходимо сначала сформировать список на основе введенной строки, а затем, каждое значение этого списка изменить, возведя в квадрат.
Отобразить результат на экране в виде строки полученных чисел, записанных через пробел. Программу следует реализовать с использованием функции enumerate.
Sample Input:
8 -11 4 3 6
Sample Output:
64 121 16 9 36
'''
# put your python code here
lst = list(map(int,input().split()))
for i in range(len(lst)):
    lst[i] = lst[i]**2
print(*lst)

