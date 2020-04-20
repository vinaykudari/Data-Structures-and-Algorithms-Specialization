# Uses python3
import sys


def no_of_inversions(l, r):
    global inversions
    lenl = len(l);
    lenr = len(r)
    n = lenl + lenr
    i = 0;
    j = 0;
    mergedList = []
    while i < lenl and j < lenr:
        if l[i] <= r[j]:
            mergedList.append(l[i])
            i += 1
        elif r[j] < l[i]:
            mergedList.append(r[j])
            j += 1
            inversions += lenl - i
        n -= 1

    for k in range(i, lenl):
        mergedList.append(l[k])

    for k in range(j, lenr):
        mergedList.append(r[k])

    #     print(f'l = {l}; r = {r}; merged list = {mergedList}')
    return mergedList


def find_inversions(lis, low, high):
    if low == high:
        return lis[low:low + 1]

    mid = low + (high - low) // 2
    left = find_inversions(lis, low, mid)
    right = find_inversions(lis, mid + 1, high)
    return no_of_inversions(left, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    inversions = 0
    find_inversions(a, 0, len(a))
    print(inversions)
