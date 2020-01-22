# Uses python3
import sys


def gcd(a, b):
    if b > a:
        a = a+b
        b = a-b
        a = a-b
    elif a == b:
        return a

    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def lcm(a, b):
    hcf = gcd(a,b)
    return int((a * b)/hcf)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

