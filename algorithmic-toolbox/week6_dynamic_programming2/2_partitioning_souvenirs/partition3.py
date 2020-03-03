# Uses python3
import sys
import itertools


def optimal_weight(W, weights):
    table = [[0 for v in range(W + 1)] for w in range(len(weights) + 1)]

    for w in range(1, len(weights) + 1):
        for v in range(W + 1):
            if v < weights[w - 1]:
                table[w][v] = table[w - 1][v]
            else:
                table[w][v] = max(table[w - 1][v], (weights[w - 1]) + table[w - 1][v - weights[w - 1]])

    return table


def trace_back(w, sum_lst, table):
    rlen = len(table)
    clen = len(table[0]) - 1
    selected_vals = []

    temp = float('inf')

    for i in reversed(range(rlen)):
        if i > temp:
            continue

        sum_lst_index = clen
        while table[i][clen] == table[i - 1][clen]:
            i = i - 1
            if i < 0:
                return selected_vals

        selected_val = w[i - 1]
        selected_vals.append(selected_val)
        clen = sum_lst[sum_lst_index] - selected_val
        temp = i

        if (i == 0) or (clen == 0):
            break

    return selected_vals


def partition3(w):
    sum_w = sum(w)
    S = int(sum_w / 3)
    temp = sum_w

    sum_lst = list(range(S + 1))
    count = 0

    if (sum_w % 3 != 0) or len(w) < 3:
        return 0

    for i in range(3):
        table = optimal_weight(S, w)
        selected_elements = trace_back(w, sum_lst, table)
        sum_selected = sum(selected_elements)

        if sum_selected == S:
            temp = temp - sum_selected
        else:
            return 0

        for element in selected_elements:
            w.remove(element)

    if temp == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

