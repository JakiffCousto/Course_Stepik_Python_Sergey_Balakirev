import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in_test = ['1 0 0 0 0',
               '0 0 1 0 0',
               '0 0 0 0 0',
               '0 1 0 1 0',
               '0 0 0 0 0']

lst_test = [list(map(int, x.strip().split())) for x in lst_in_test]


def is_isolate(lst_in, i, j):
    key = True
    if (lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][j + 1]) > 1:
        key = False
    return key


def verify(args):
    key = True
    for u in range(len(args)-1):
        for v in range(len(args[u])-1):
            if not is_isolate(args, u, v):
                key = False
                break
    return key


print(verify(lst_test))
