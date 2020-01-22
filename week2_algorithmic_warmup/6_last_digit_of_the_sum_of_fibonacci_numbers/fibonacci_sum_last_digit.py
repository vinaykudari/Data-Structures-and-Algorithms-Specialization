# Uses python3
import sys


def fib_sum_last(m):
    s=1
    if m==0:
        return 0
    a = 0
    b = 1
    for i in range(1, m):
        temp = b%10
        b = (a + b%10)
        a = temp
        s = (s + b)%10
    return s


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_last(n))
