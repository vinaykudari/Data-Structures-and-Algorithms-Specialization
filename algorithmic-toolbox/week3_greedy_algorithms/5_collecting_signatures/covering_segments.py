# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments.sort(key=lambda x: x[1], reverse=True)
    min_points = []
    for i in range(len(segments)):
        if not min_points:
            min_points.append(segments[i].start)
        elif segments[i].start > min_points[-1]:
            min_points[-1] = segments[i].start
        elif segments[i].end < min_points[-1]:
            min_points.append(segments[i].start)

    return min_points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
