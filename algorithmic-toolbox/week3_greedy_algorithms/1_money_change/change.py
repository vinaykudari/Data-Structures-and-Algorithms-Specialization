# Uses python3
import sys


def get_change(m):
    # write your code here\
    mmod = m % 10
    return int(m/10) + int(mmod / 5) + (mmod % 5)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
