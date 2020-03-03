# Uses python3
import sys


def get_optimal_value(cap, weights, vals):
    value = 0.
    # write your code here
    best_vals = [vals[i] / weights[i] for i in range(len(vals))]
    temp = []
    while len(best_vals) > 0 and cap > 0:
        if len(best_vals) == 1:
            index = 0
        else:
            index = best_vals.index(max(best_vals))

        if weights[index] <= cap:
            temp.append(vals[index])
            cap = cap - weights[index]
            best_vals.pop(index)
            weights.pop(index)
            vals.pop(index)
        else:
            temp.append((vals[index] / weights[index]) * cap)
            cap = 0

    return round(sum(temp), 3)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
