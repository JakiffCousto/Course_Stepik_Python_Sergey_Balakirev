"""Decorators of function with parameters"""
from functools import wraps
import math


def df_decorator(dx=0.001):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator(dx=0.0000001)
def sin_df(x):
    """Function for calculating derivative of sin"""
    return math.sin(x)


dsin_dx = sin_df(math.pi / 4)
print(dsin_dx)
print(sin_df.__name__)  # output the name of function
print(sin_df.__doc__)


def cos_df(x):
    return math.cos(x)


f = df_decorator(dx=0.0001)  # call outer function df_decorator
s = f(cos_df)
a = s(math.pi / 4)
print(a)


def tan_df(x):
    return math.tan(x)


tan_df = df_decorator(dx=0.01)(tan_df)  # call outer function df_decorator
print(tan_df(math.pi / 4))
