'''
Подвиг 6.
Вводится целое положительное число a. Необходимо определить генератор,
который бы возвращал модули чисел в диапазоне [-a; a], а затем еще один,
который бы вычислял кубы чисел (возведение в степень 3), возвращаемых первым генератором.
Вывести в одну строчку через пробел первые четыре значения. (Полагается, что генератор выдает, как минимум четыре значения).
'''

# put your python code here
a = int(input())
gen_1 = (abs(x) for x in range(-a, a))
gen_2 = (x**3 for x in gen_1)
i = 0
for element in gen_2:
    i = i + 1
    print(element, end=' ')
    if i > 3:
        break