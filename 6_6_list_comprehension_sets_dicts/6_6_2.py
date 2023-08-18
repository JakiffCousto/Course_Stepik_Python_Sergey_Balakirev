'''
Подвиг 3.
На автомойку в течение квартала заезжали машины.
Их гос. номера фиксировались в журнале, следующим образом (пример):
Е220СК
А120МВ
В101АА
Е220СК
А120МВ
На основе такого списка через генератор множеств сформировать список уникальных машин.
На экран вывести число уникальных машин.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
А323ГД
Д456ВВ
Б001ББ
Д456ВВ
С111СС
Sample Output:
4
'''
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
s = {x for x in lst_in}
print(len(s))
# здесь продолжайте программу (используйте список lst_in)