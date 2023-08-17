'''
Подвиг 5.
Вводятся данные в формате ключ=значение в одну строчку через пробел.
Необходимо на их основе создать словарь, затем проверить,
существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки).
Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
Sample Input:
вологда=город house=дом True=1 5=отлично 9=божественно
Sample Output:
ДА
'''
lst_in = list(map(str, input().split()))
A = [a.split('=') for a in lst_in]
my_dick = dict(A)
my_list = ['house', 'True', '5']
c = 0

for element in my_list:
    if element in my_dick:
        c = c + 1
if c == 3:
    print("ДА")
else:
    print("НЕТ")
