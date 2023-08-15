'''
Подвиг 9.
Вводится список названий городов в одну строчку через пробел.
Перебрать все эти названия с помощью цикла for и определить,
начинается ли название следующего города на последнюю букву предыдущего города в списке.
Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква.
Вывести на экран ДА, если последовательность удовлетворяет этому правилу и НЕТ - в противном случае.
Sample Input:
Москва Астрахань Новгород Димитровград Душанбе
Sample Output:
ДА
'''

lst_in = list(map(str, input().lower().split()))
key = 'ДА'
for i in range(len(lst_in) - 1):
    if lst_in[i][-1] == 'ь' or lst_in[i][-1] == 'ъ' or lst_in[i][-1] == 'ы':
        if lst_in[i + 1][0] != lst_in[i][-2]:
            key = 'НЕТ'
            break
    else:
        if lst_in[i + 1][0] != lst_in[i][-1]:
            key = 'НЕТ'
            break
print(key)

