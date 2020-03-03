# Uses python3
import sys


def optimal_weight(W, weights):
    table = [[0 for v in range(W + 1)] for w in range(len(weights) + 1)]

    for w in range(1, len(weights) + 1):
        for v in range(W + 1):
            if v < weights[w - 1]:
                table[w][v] = table[w - 1][v]
            else:
                table[w][v] = max(table[w - 1][v], (weights[w - 1]) + table[w - 1][v - weights[w - 1]])

    return table[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
