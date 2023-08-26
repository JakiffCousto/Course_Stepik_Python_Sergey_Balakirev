'''
Пример из теории
'''


cities = ['New York', 'Boston', 'Chicago']
b = map(lambda s: list(s.lower()), cities)
c = map(lambda s: s[::-1], cities)

d = list(b)
a = list(c)
print(d)
print(a)

