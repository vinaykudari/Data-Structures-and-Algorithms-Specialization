#Uses python3

import sys


def number_of_components(n, m, edges):
    connected_components = 0
    graph, visited_nodes = {}, {}
    related_nodes = []
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]

    for i in range(1, n+1):
        if i not in visited_nodes:
            connected_components += 1
            visited_nodes[i] = True
            if i in graph:
                related_nodes = graph[i]
                del graph[i]
                j, L = 0, len(related_nodes)
                while j < L:
                    visited_nodes[related_nodes[j]] = True
                    if related_nodes[j] in graph:
                        related_nodes += graph[related_nodes[j]]
                        L += len(graph[related_nodes[j]])
                        del graph[related_nodes[j]]
                    j += 1

    return connected_components


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print(number_of_components(n, m, edges))
