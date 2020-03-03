# Uses python3
import sys


def get_majority_element(a, left, right):
    dic = {}
    l = len(a)

    for i in a:
        if i in dic.keys():
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    for key, value in dic.items():
        if value > l/2:
            return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))
