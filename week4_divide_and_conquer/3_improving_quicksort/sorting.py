# Uses python3
import sys
import random


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition3(a, left, right):
    x = a[left]
    lt = left
    gt = right
    i = left
    while i <= gt:
        if a[i] < x:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > x:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    partition_index_l, partition_index_r = partition3(a, l, r)
    randomized_quick_sort(a, l, partition_index_l - 1)
    randomized_quick_sort(a, partition_index_r + 1, r)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
