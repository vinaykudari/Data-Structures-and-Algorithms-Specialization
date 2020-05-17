#Uses python3

import sys


def acyclic(adj):
    visited = [0]*len(adj)
    recStack = visited
    for i in range(len(adj)):
        if not visited[i]:
            if explore(adj, i, visited, recStack):
                return 1
    return 0


def explore(adj, i, visited, recStack):
    visited[i] = 1
    recStack[i] = 1
    for j in range(len(adj[i])):
        if not visited[adj[i][j]]:
            # print(f'visiting {adj[i][j]} in {adj[i]}')
            if explore(adj, adj[i][j], visited, recStack):
                return 1
        elif recStack[i]:
            return 1
    recStack[i] = 0
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    # print(adj)
    print(acyclic(adj))
