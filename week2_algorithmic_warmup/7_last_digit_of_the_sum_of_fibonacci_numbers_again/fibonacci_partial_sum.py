# Uses python3
import sys


def fib_upto(m):
    lis = [0,1]
    for i in range(1, m):
        lis.append( ((lis[i]%10) + (lis[i-1]%10))%10 )
    return lis


def fib_sum_again(m, n):
    if m==n:
        lis = fib_upto(m)
        return lis[m]%10
    else:
        lis = fib_upto(n)
        return sum(lis[m:n+1])%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_sum_again(from_, to))
