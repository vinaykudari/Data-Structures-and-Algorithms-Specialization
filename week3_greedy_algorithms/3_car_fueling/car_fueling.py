# python3
import sys


def compute_min_refills(td, max_distance, stops):
    md = max_distance
    refuel = 0
    stops.append(td)

    for i in range(len(stops)):
        dist_travelled = stops[i]
        distance_left = max_distance - dist_travelled

        #         print(f"stop = {stops[i]};  distance_left = {distance_left}; i = {i}")

        if i < len(stops) - 1:

            if distance_left < stops[i + 1] - stops[i]:
                max_distance = stops[i] + md
                refuel = refuel + 1
                #                 print(f"refueled {refuel} time")
                if max_distance - dist_travelled < stops[i + 1] - stops[i]:
                    return -1

    return refuel


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
