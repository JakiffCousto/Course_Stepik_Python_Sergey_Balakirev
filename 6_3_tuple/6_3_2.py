'''
Подвиг 4.
Вводятся названия городов в одну строку через пробел.
На их основе формируется кортеж. Если в этом кортеже нет города "Москва",
то следует его добавить в конец кортежа.
Результат вывести на экран в виде строки с названиями городов через пробел.
Sample Input:
Уфа Казань Самара
Sample Output:
Уфа Казань Самара Москва
'''
lst_in = input().split()
t = tuple(lst_in)
if "Москва" not in t:
    t = t + ("Москва",)
print(*t)