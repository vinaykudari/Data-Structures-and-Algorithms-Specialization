# Uses python3
import sys


def optimal_sequence(n):
    arr = [0] * (n + 1)

    if n == 1:
        return [1]

    arr[1] = 1

    temp = {}
    lis = [n]
    head = n

    for i in range(2, n + 1):
        if i < 4:
            arr[i] = 1
            temp[i] = 1
        elif i % 2 == 0 and i % 3 != 0:
            i2 = i // 2
            im = i - 1
            arr[i] = min(arr[i2] + 1, arr[im] + 1)
            if arr[i2] < arr[im]:
                temp[i] = i2
            else:
                temp[i] = im
        elif i % 3 == 0 and i % 2 != 0:
            i3 = i // 3
            im = i - 1
            arr[i] = min(arr[i3] + 1, arr[im] + 1)
            if arr[i3] < arr[im]:
                temp[i] = i3
            else:
                temp[i] = im
        elif i % 3 != 0 and i % 2 != 0:
            arr[i] = arr[i - 1] + 1
            temp[i] = i - 1
        else:
            i2 = i // 2
            i3 = i // 3
            arr[i] = min(arr[i2] + 1, arr[i3] + 1)
            if arr[i2] < arr[i3]:
                temp[i] = i2
            else:
                temp[i] = i3

    while head != 1:
        head = temp.get(head)
        lis.append(head)

    return reversed(lis)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
