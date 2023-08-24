import math


def func_decorator(func, dx=0.0001):
    def wrapper(x, *args, **kwargs):
        res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return res

    return wrapper


def sin_df(x):
    return math.sin(x)


sin_df = func_decorator(sin_df, dx=0.01)

df = sin_df(math.pi / 4)
print(df)
