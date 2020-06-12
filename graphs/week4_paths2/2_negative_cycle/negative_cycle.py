#Uses python3

import sys
import math


def negative_cycle(adj, cost):
    dist, no_of_edges = {}, len(adj)

    for i in range(no_of_edges):
        dist[i] = 10000000

    dist[0] = 0

    for i in range(no_of_edges):
        for u in range(no_of_edges):
            for v in range(len(adj[u])):
                if dist[adj[u][v]] > dist[u] + cost[u][v]:
                    # edge relaxing on Vth iteration
                    if i == no_of_edges-1:
                        return 1
                    dist[adj[u][v]] = dist[u] + cost[u][v]
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
