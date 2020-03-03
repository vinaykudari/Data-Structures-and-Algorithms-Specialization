# Uses python3
import sys


def optimal_summands(n):
    summands = []
    m = 1
    while n - m > m:
        summands.append(m)
        n = n - m
        m = m + 1

    if n > 0:
        summands.append(n)

    return list(set(summands))


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
