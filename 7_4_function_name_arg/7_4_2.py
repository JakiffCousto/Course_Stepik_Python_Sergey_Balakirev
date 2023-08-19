'''
Подвиг 3.
Объявите функцию с именем check_password,
которая принимает аргумент - строку (пароль)
и имеет один формальный параметр chars с начальным
значением в виде строки "$%!?@#". Функция должна проверять:
есть ли в пароле хотя бы один символ из chars и что длина пароля
не менее 8 символов. Если проверка проходит, то функция возвращает True, иначе - False.
P. S. Вызывать функцию не нужно, только объявить.
Sample Input:
12345678!
Sample Output:
True
'''


def check_password(password, chars="$%!?@#"):
    key = False
    for i in chars:
        if i in password and len(password) >= 8:
            key = True
    return key