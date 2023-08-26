"""
Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
"""


def get_prime():
    i = 2
    while True:
        key = True
        if i == 0 or i == 1:
            key = False
            for j in range(2, i):
                if i % j == 0:
                    key = False
        if key:
            yield i
            i = i + 1


# for i in range(20):
#     print(next(get_prime()), end=' ')

g = get_prime()
c = 1
for k in g:
    if c == 20:
        break
    print(k, end=' ')
    c = c + 1
