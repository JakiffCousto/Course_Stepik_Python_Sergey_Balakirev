'''
Подвиг 5.
Вводится список email-адресов в одну строчку через пробел.
Среди них нужно оставить только корректно записанные адреса.
Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
Результат отобразить в виде строки email-адресов, записанных через пробел.
=============
Sample Input:
abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
=============
Sample Output:
abc@it.ru biba123@list.ru sc_lib@list.ru
'''
from string import ascii_letters

chars = ascii_letters + "0123456789_@."

s = "abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com"
a = s.split()

t = list(s[0])
print(t)


def symbols(w):
    for x in w:
        for y in x:
            if y not in chars:
                return False
        return True


q = filter(symbols, a)
d = filter(lambda x: x.index('.') - x.index('@')>1, q)
print(list(d))

