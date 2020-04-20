#Uses python3

import sys


def lcs2(a, b):
    lenA = len(a);
    lenB = len(b)
    grid = [[0 for j in range(lenB + 1)] for i in range(lenA + 1)]
    for i in range(1, lenA + 1):
        for j in range(1, lenB + 1):
            if a[i - 1] == b[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])

    return grid[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
