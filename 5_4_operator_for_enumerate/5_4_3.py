'''
Большой подвиг 3.
В виде строки записано арифметическое выражение, например:
"10 + 25 - 12"
или
"10 + 25 - 12 + 20 - 1 + 3"
и т. д. То есть, количество действий может быть разным.
Необходимо выполнить вычисление и результат отобразить на экране.
Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-),
а в качестве операндов - целые неотрицательные числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
Sample Input:
10+25 - 12
Sample Output:
23
'''
# my option
str_calc = input()
str_2 = str_calc.replace(' ', '')
result = 0
lst_action = []
lst_action_index = []
for i in range(len(str_2)-1):
    if not str_2[i].isdigit():
        lst_action.append(str_2[i])
        lst_action_index.append(i)
result = int(str_2[0:lst_action_index[0]])
for j in range(len(lst_action_index)-1):
    result = result + int(str_2[lst_action_index[j]:lst_action_index[j+1]])
result = result + int(str_2[lst_action_index[-1]:])
print(result)

# Владислав Мальцев option
text = input().replace(' ', '').replace('-', '+-').split('+')
print(sum(map(int, text)))