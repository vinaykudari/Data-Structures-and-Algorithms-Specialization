# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    min = float('inf')
    dic = {}
    lis = []
    segment_length = len(segments)
    for segment in segments:
        for i in range(segment.start, segment.end + 1):
            if i in dic.keys():
                dic_len = len(dic[i])
                if dic_len == 0:
                    return i
                if dic_len < min:
                    min = dic_len
                    min_key = i
                if segments.index(segment) in dic[i]:
                    dic[i].remove(segments.index(segment))

            else:
                dic[i] = list(range(len(segments)))
                dic[i].remove(segments.index(segment))

    lis.append(min_key)

    for j in dic[min_key]:
        lis.append(segments[j].end)

    list(set(lis)).sort()

    return list(set(lis))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
