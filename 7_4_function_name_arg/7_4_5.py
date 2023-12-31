'''
Подвиг 6.
Функции из предыдущего подвига 5 добавьте еще один формальный
параметр up с начальным булевым значением True.
Если параметр up равен True, то тег (указанный в формальном параметре tag)
следует записывать заглавными буквами, а иначе - малыми.
После объявления функции прочитайте (с помощью функции input)
строку и дважды вызовите функцию (с выводом результата ее работы на экран):
- первый раз со строкой и именованным аргументом tag со значением 'div'
- второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
Sample Input:
Python is best!
Sample Output:
<DIV>Python is best!</DIV>
<div>Python is best!</div>
'''


# put your python code here
def get_teg(text, t="h1", up=True):
    if up == True:
        t = t.upper()
        str_out = "<" + t + ">" + text + "</" + t + ">"
    else:
        str_out = "<" + t + ">" + text + "</" + t + ">"
    return str_out


str_in = input()
print(get_teg(str_in, t="div", up=True))
print(get_teg(str_in, t="div", up=False))
