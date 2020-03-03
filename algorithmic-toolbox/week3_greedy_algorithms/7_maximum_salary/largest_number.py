# Uses python3

import sys


def get_max(a, b):
    ab = a + b
    ba = b + a
    if int(ab) >= int(ba):
        return a
    elif int(ba) >= int(ab):
        return b


def largest_number(a):
    max_lis = []
    l = len(a)
    while len(max_lis) < l:
        max = str(a[0])
        for i in a:
            max = get_max(i, max)
        max_lis.append(max)
        a.remove(max)
    return int(''.join(max_lis))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
