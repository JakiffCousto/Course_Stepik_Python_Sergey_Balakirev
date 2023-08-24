from functools import wraps

def inner_decorator(func):
    @wraps(func)
    def wrapper(*args):
        fin = sum(func(*args))
        return fin
    return wrapper

@inner_decorator
def get_list(s: str):
    """Функция для формирования списка целых значений"""
    res = list(map(int, s.split()))
    return res


s_test = '1 3 5 7 11'
print(get_list(s_test))
print(get_list.__doc__)