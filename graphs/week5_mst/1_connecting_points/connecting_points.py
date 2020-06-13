#Uses python3
import sys
import math
import heapq


def minimum_distance(x, y):
    N = len(x)
    heap = []

    cost = [float('inf')] * N
    parent = [None] * N

    cost[0] = 0
    total_cost = 0
    nodes_to_check = list(range(N))

    for i in range(N):
        heapq.heappush(heap, (cost[i], i))

    while heap:
        uCost, uIndex = heapq.heappop(heap)
        if uIndex in nodes_to_check:
            nodes_to_check.remove(uIndex)
        if uCost > cost[uIndex]:
            continue
        total_cost += uCost
        for vIndex in nodes_to_check:
            vCost = get_dist(x[uIndex], y[uIndex], x[vIndex], y[vIndex])
            if cost[vIndex] > vCost:
                cost[vIndex] = vCost
                parent[vIndex] = uIndex
                heapq.heappush(heap, (vCost, vIndex))

    return total_cost


def get_dist(x1, y1, x2, y2):
    return math.sqrt(math.pow((y2-y1), 2) + math.pow((x2-x1), 2))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
