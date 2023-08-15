'''
Подвиг 9.
(На использование цикла while).
Вводятся названия книг (каждое с новой строки).
Удалить из введенного списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом).
Результат вывести на экран в виде строки из оставшихся названий через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки
Sample Input:
Муму
Евгений Онегин
Сияние
Мастер и Маргарита
Пиковая дама
Колобок
Sample Output:
Муму Сияние Колобок
'''
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список lst_in)
i = 0
lst_out = []
while i < len(lst_in):
    if ' ' in lst_in[i]:
        element = lst_in.pop(i)
        i = i - 1
    i = i + 1
print(*lst_in)