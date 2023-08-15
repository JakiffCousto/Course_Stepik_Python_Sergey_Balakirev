'''
Подвиг 6.
Вводится строка (слаг).
Замените в этой строке все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-).
Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.
Sample Input:
osnovnye--metody-----slovarey
Sample Output:
osnovnye-metody-slovarey
'''

new_string=input()
while "--" in new_string:
    new_string=new_string.replace("--","-")
print(new_string)

