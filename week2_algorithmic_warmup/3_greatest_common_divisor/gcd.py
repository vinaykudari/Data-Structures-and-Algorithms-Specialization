# Uses python3
import sys


def gcd(n1, n2):
    if n2 == 0:
        print(n1)
        return

    if n1 > n2:
        r = n1 % n2
        gcd(n2, r)
    elif n1 < n2:
        r = n2 % n1
        gcd(n1, r)
    else:
        print(n1)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    gcd(a, b)
