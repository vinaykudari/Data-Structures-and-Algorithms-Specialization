# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    lis = [];
    start_count = 0;
    dic = {}
    for i in range(len(starts)):
        lis.append((starts[i], 'a'))
        lis.append((ends[i], 'c'))

    for i in range(len(points)):
        lis.append((points[i], 'b'))

    lis.sort()
    #     print(lis)

    for item in lis:
        ty = item[1]
        if 'a' == ty:
            start_count += 1
        elif 'b' == ty:
            dic[item[0]] = start_count
        elif 'c' == ty:
            start_count -= 1

    lis = [dic[point] for point in points]
    return lis


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
