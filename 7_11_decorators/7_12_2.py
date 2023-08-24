'''
Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
Определите декоратор для этой функции, который имеет один параметр tag,
определяющий строку с названием тега и начальным значением "h1".
Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
Пример заключения строки "python" в тег h1: <h1>python</h1>
Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.
Sample Input:
Декораторы - это классно!
Sample Output:
<div>декораторы - это классно!</div>
'''

def outer_decorator(tag = "h1"):
    def inner_decorator(func):
        def wrapper(*args):
            print('<'+tag+'>'+func(*args)+'</'+tag+'>')
        return wrapper
    return inner_decorator


@outer_decorator(tag = "h1")
def get_s(s_input:str):
    return s_input.lower()

s_test = "Python"

get_s(s_test)