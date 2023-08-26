'''
Подвиг 1.
Вводятся названия городов в одну строчку через пробел.
Необходимо определить функцию filter, которая бы возвращала только названия длиной более 5 символов.
Извлеките первые три полученных значения с помощью функции next и отобразите их на экране в одну строчку через пробел.
(Полагается, что минимум три значения имеются).
================
Sample Input:
Тула Ульяновск Хабаровск Владивосток Омск Уфа
================
Sample Output:
Ульяновск Хабаровск Владивосток
'''

s = 'Тула Ульяновск Хабаровск Владивосток Омск Уфа'
f = filter(lambda x: len(x) > 5, s.split())
print(next(f))
print(next(f))
print(next(f))