'''
Подвиг 8.
Пользователь с клавиатуры вводит названия городов, пока не введет букву q.
Определить общее уникальное число городов, которые вводил пользователь.
На экран вывести это число. Из коллекций при реализации программы использовать только множества.
Sample Input:
Уфа
Москва
Тверь
Екатеринбург
Томск
Уфа
Москва
q
Sample Output:
5
'''
town_set = set()
while True:
    town_input = input()
    if town_input != 'q':
        town_set.add(town_input)
    else:
        break
print(len(town_set))