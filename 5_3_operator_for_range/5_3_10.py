'''
Подвиг 10.
Вводится натуральное число n.
Вычислить сумму всех натуральных чисел меньше n, которые кратны или 3 или 5.
Результат (сумму) вывести на экран. Пример: n = 10, имеем числа: 3, 5, 6, 9.
Их сумма равна 23.
Sample Input:
21
Sample Output:
98
'''
# put your python code here
n = int(input())
sum = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print(sum)

