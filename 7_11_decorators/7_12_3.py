t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
     ' ': '-', '-': '-'}


def outer_decorator(chars="?!"):
    def inner_decorator(func):
        fin = ''

        def wrapper(x):
            nonlocal fin
            y = func(x)
            j = 0
            while j < len(y):
                if y[j] in chars:
                    fin = fin + '-'
                if y[j] != "-" and y[j] not in chars:
                    fin = fin + y[j]
                elif y[j] == "-" and y[j + 1] != "-":
                    fin = fin + y[j]
                elif y[j] == ' ':
                    fin = fin + '-'
                j = j + 1
            return fin

        return wrapper
    return inner_decorator


@outer_decorator(chars="?!:;,. ")
def convert_lat(s: str):
    a = s.lower()
    res = ''
    for element in a:
        res = res + t.get(element, element)
    return res


s_test = "!Декораторы - это круто!"
print(convert_lat(s_test))
