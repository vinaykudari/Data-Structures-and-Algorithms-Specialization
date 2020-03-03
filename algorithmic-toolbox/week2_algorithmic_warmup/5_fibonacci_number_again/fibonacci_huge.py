# Uses python3
import sys


def fib_rep(n, m):
    lis = [0, 1]
    count, i = 0, 2
    flag = True
    while flag:
        lis.append((lis[-1] + lis[-2])%m)
        if lis[-1] == 0 and lis[-2] == 1:
            count = count + 1
        if count == 1:
            flag = False
        i = i+1
    return lis[n % (i-1)]
    

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib_rep(n, m))
