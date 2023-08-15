'''
Подвиг 5.
Вводится список в виде целых чисел в одну строку через пробел.
Сначала нужно сформировать список из введенной строки.
Затем, каждый элемент этого списка продублировать один раз.
Результат отобразить на экране в виде строки полученных чисел, записанных через пробел.
Sample Input:
8 11 2
Sample Output:
8 8 11 11 2 2
'''
# put your python code here
lst = list(map(int, input().split()))
lst_result = []
for i in range(len(lst)):
    num = lst[i]
    lst_result.append(num)
    lst_result.append(num)
print(*lst_result)

