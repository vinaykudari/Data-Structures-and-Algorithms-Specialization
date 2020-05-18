#Uses python3

import sys
from _collections import deque


def bipartite(adj):
    # print(f'adj={adj}')
    depth, color = {}, {}

    for i in range(len(adj)):
        depth[i] = float('inf')
        color[i] = -1

    visited, depth[0] = deque(), 0
    visited.append(0)

    while visited:
        u = visited.popleft()
        # print(f'u={u}')
        if color[u] == -1:
            color[u] = False

        for v in adj[u]:
            # print(f'u={u}, v={v}')
            if color[u] == color[v]:
                return 0
            if depth[v] == float('inf'):
                visited.append(v)
                depth[v] = depth[u] + 1
                color[v] = not color[u]

        # print(color, visited)

    return 1


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
    print(bipartite(adj))
