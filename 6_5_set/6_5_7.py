'''
Подвиг 7.
Вводится натуральное число, которое может содержать только простые множители 1, 2, 3, 5 и 7
(любые из них, необязательно все).
Необходимо разложить введенное число на простые множители и проверить,
содержит ли оно множители 2, 3 и 5 (обязательно все их, хотя бы один раз).
Если это так, то вывести ДА, иначе - НЕТ.
Sample Input:
210
Sample Output:
ДА
'''
s = {2, 3, 5}
N = int(input())
sum = 0
for i in s:
    c = N % i
    sum = sum + c
if sum == 0:
    print("ДА")
else:
    print("НЕТ")