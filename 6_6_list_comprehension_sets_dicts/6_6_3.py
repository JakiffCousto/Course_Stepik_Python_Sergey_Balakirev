'''
Подвиг 4.
Вводится текст в одну строчку со словами через пробел.
С помощью генератора множеств сформировать множество из уникальных слов
без учета регистра и длина которых не менее трех символов. Вывести на экран размер этого множества.
Sample Input:
Хижина изба машина и снова хижина машина
Sample Output:
4
'''
lst_in = input().lower().split()
s = {x for x in lst_in if len(x) > 2}
print(len(s))
