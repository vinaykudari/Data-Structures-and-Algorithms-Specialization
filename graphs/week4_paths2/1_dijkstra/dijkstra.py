# Uses python3

import sys
import queue
import heapq


def distance(adj, cost, s, t):
    dist, prev = {}, {}
    heap = []

    for i in range(len(adj)):
        dist[i] = float('inf')
    dist[s] = 0

    for node_index, distance_from_origin in dist.items():
        heapq.heappush(heap, (distance_from_origin, node_index))

    while heap:
        min_node_distance, min_node_index = heapq.heappop(heap)

        # to account for duplicate addition of (dist, node) into heap)
        if min_node_distance > dist[min_node_index]:
            continue

        for v_index in range(len(adj[min_node_index])):
            new_distance = min_node_distance + cost[min_node_index][v_index]
            if new_distance < dist[adj[min_node_index][v_index]]:
                dist[adj[min_node_index][v_index]] = new_distance
                prev[adj[min_node_index][v_index]] = min_node_index
                # hack to overcome changePriority
                heapq.heappush(heap, (new_distance, adj[min_node_index][v_index]))

    return dist[t] if dist[t] != float('inf') else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
