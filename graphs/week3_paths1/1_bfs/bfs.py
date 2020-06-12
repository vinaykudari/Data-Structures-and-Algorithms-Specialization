#Uses python3

import sys
from _collections import deque


def distance(adj, s, t):
    # print(adj)
    dist, prev = {}, {}
    simpleQueue = deque()

    for i in range(len(adj)):
        dist[i] = float('inf')
        prev[i] = None

    # considering sth node as vertex
    dist[s] = 0
    simpleQueue.append(s)

    while simpleQueue:
        u = simpleQueue.popleft()
        # print(f'u={u}, adj[u]={adj[u]}')
        for v in adj[u]:
            if dist[v] == float('inf'):
                simpleQueue.append(v)
                dist[v] = dist[u] + 1
                prev[v] = u

    if dist[t] != float('inf'):
        return dist[t]

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
