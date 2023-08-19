def get_data_fig(*args, **kwargs):
    data = {"type": None, "color": None, "closed": None, "width": None}
    p = 0
    for i in args:
        p = p + i
    lst = [p]
    for kd in data:
        for kw in kwargs:
            if kd == kw:
                lst.append(kwargs[kw])
    return tuple(lst)


print(get_data_fig(3, 4, 5, type=True, color="Yellow", closed=False, width=5))
print(get_data_fig(3, 4, 5, color=256, closed=False, width=5, type=True))
print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))
