'''
Подвиг 8.
Напишите функцию, которая проверяет корректность
переданного ей email-адреса в виде строки.
Будем полагать, что адрес верен, если он обязательно содержит
символы '@' и '.', а все остальные символы могут принимать значения:
'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.
После объявления функции прочитайте (с помощью функции input)
строку с email-адресом и вызовите функцию с этим аргументом.
Sample Input:
sc_lib@list.ru
Sample Output:
ДА
'''
def check_email(x):
    t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y',
         'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@',
         '.'}
    s = set(x)
    if s < t:
        print("ДА")
    else:
        print("НЕТ")


str_in = input()
check_email(str_in)
