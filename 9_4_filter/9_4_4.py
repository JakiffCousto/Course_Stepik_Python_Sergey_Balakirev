'''
Подвиг 4.
Саша и Галя коллекционируют монетки.
Каждый из них решил записать номиналы монеток из своей коллекции.
Получилось два списка.
Эти списки поступают на вход программы в виде двух строк из целых чисел,
записанных через пробел.
Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные.
Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
==================
Sample Input:
1 5 2 7 10 25 50 100
5 2 3 7 10 25 55
==================
Sample Output:
2 10
'''
s_1 = '1 5 2 7 10 25 50 100'
s_2 = '5 2 3 7 10 25 55'
a = list(map(int, s_1.split()))
b = list(map(int, s_2.split()))
g = [x for x in a and b]
f = filter(lambda x: x%2 == 0, g)
res = list(f)
r = sorted(res)
print(*r)

print(*filter(lambda a: int(a) % 2 == 0, set(a)&set(b)))
