import re
from math import inf


def main(file_name, y):
    devices, sensors, beacons = set(), dict(), set()
    min_row, max_row, min_col, max_col = inf, -inf, inf, -inf
    with open(file_name, 'r') as infile:
        for line in infile:
            line = [x for x in re.sub("[\sa-zA-Z:,]+", '', line[12:]).split('=')]
            line = list(map(int, line))
            # print(line)
            min_row, max_row = min(min_row, line[1], line[3]), max(max_row, line[1], line[3]),
            min_col, max_col = min(min_col, line[0], line[2]), max(max_col, line[0], line[2])
            man_hat_dist = abs(line[3] - line[1]) + abs(line[2] - line[0])
            # print(man_hat_dist)
            # rows, cols = max_row-min_row+1, +1
            sensors[(line[1], line[0])] = man_hat_dist
            beacons.add((line[3], line[2]))
            devices.add((line[1], line[0])), devices.add((line[3], line[2]))
    # print(min_row, max_row, min_col, max_col)
    # print(sensors)
    # print(beacons)

    spaces_in_range = 0
    # for x in range(min_col, max_col+1):
    #     # print(f"row: {y}  col: {x}")
    #     if (y, x) in devices:
    #         # print('device: ', (y, x))
    #         continue
    #
    #     in_range = False
    #     for sensor, dist in sensors.items():
    #         man_hat_dist = abs(sensor[1] - x) + abs(sensor[0] - y)
    #         if man_hat_dist <= dist:
    #             # print(f"sensor {sensor}, dist {dist}, man-hat: {man_hat_dist}")
    #             in_range = True
    #             break
    #     spaces_in_range += 1 * (in_range)
    #     # print(in_range)

    spaces_two, in_range_set = 0, set()
    for sensor, dist in sensors.items():
        # print(sensor, dist)
        dist_to_y = abs(y - sensor[0])
        if dist_to_y > dist:
            continue
        # print(sensor, dist)
        # print("valid y: ", abs(y - sensor[0]))
        left_overs = dist - dist_to_y
        for x in range(sensor[1]-left_overs,sensor[1]+left_overs+1):
            if (y,x) not in beacons:
                in_range_set.add((y, x))
    # print(sorted(in_range_set))
    return spaces_in_range, len(in_range_set)



# print(main("AOC22_D15_inp0.txt", 10))
print(main("AOC22_D15_inp.txt", 2000000))
# 3869895 too low
