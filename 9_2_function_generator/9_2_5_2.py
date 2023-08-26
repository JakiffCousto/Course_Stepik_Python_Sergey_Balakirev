"""
Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
"""


def prime():
    i = 1
    while True:
        i = i + 1
        key = True
        if i == 0:
            key = False
        for j in range(2, i):
            if i % j == 0:
                key = False
        if key:
            yield i


c = 1
for element in prime():
    if c > 20:
        break
    print(element, end=' ')
    c = c + 1
