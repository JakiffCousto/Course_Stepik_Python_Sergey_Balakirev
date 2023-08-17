'''
Подвиг 3.
Вводятся данные в формате ключ=значение в одну строчку через пробел.
Значениями здесь являются целые числа (см. пример ниже).
Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:
print(*sorted(d.items()))
Sample Input:
one=1 two=2 three=3
Sample Output:
('one', 1) ('three', 3) ('two', 2)
'''
s = "one=1 two=2 three=3"
lst_in = (s.split())
A = []
print(s)
for x in lst_in:
    A.append(x.split('='))
    print(A)
for j in range(len(A)):
    A[j][1] = int(A[j][1])
    print("2",A)
dick = dict(A)
print(*sorted(dick.items()))