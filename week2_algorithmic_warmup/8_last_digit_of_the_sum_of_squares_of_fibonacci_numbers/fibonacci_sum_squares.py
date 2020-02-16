# Uses python3
from sys import stdin


def fib_last(n):
    lis = [0, 1]
    if n > 60:
        n = (n%60) + 60
    while n - 2 > 0:
        lis.append(lis[-1]%10 + lis[-2]%10)
        lis.remove(lis[0])
        n = n-1
    sum = (lis[-1]%10 + lis[-2]%10)%10
    return sum


def fibonacci_sum_squares_naive(n):
    if n==0:
        res=0
    else:
        res = fib_last(n) * fib_last(n+1)
    return res % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
