#Uses python3

import sys


def reach(n, m, edges, x, y):
    graph = {}
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]

    # print(graph)
    if x in graph:
        search_list = list(set(graph[x]))
        i, L = 0, len(search_list)
        del graph[x]
        while i < L:
            if y == search_list[i]:
                return 1
            if search_list[i] in graph:
                search_list = search_list + list(set(graph[search_list[i]]))
                L += len(list(set(graph[search_list[i]])))
                del graph[search_list[i]]
            i += 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[-2:]
    print(reach(n, m, edges, x, y))
