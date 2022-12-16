import re
from math import inf
from time_this import time_this


def main(file_name, y, max_size):
    sensors = dict()
    with open(file_name, 'r') as infile:
        for line in infile:
            line = list(map(int, [x for x in re.sub("[\sa-zA-Z:,]+", '', line[12:]).split('=')]))
            man_hat_dist = abs(line[3] - line[1]) + abs(line[2] - line[0])
            sensors[(line[1], line[0])] = man_hat_dist
    location = find_signal(sensors, max_size)
    return location[1] * 4000000 + location[0]


def find_signal(sensors, max_size):
    for row in range(max_size, -1, -1):
        found, col = check_row(sensors, max_size, row)
        if found:
            return row, col


def check_row(sensors, max_size, i):
    """ Two pointers?....no....Four pointers
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    From Left ->    <-To-Left <----> To-Right ->    <-From-Right
                                /\
                                |
                         Dist from source    
    """
    from_left, from_right, to_left, to_right = -inf, inf, None, None
    # Sort sensors by leftmost x for row; merge intervals
    for sensor, dist in sorted(sensors.items(), key=lambda k: k[0][1] - abs(k[1] - abs(i - k[0][0]))):
        x, y = sensor[1], sensor[0]
        dist_to_y = abs(i - y)
        left_over = dist - dist_to_y
        if left_over < 0:
            continue

        if to_left is None:
            to_left, to_right = x - left_over, x + left_over
        elif to_left <= x - left_over <= to_right or to_left <= x + left_over <= to_right:
            to_left, to_right = min(to_left, x - left_over), max(to_right, x + left_over)
        if x - left_over <= 0 or x - left_over <= from_left:
            from_left = max(from_left, x + left_over)
        if x + left_over >= max_size or x + left_over >= from_right:
            from_right = min(from_right, x - left_over)

        from_left = to_right if from_left >= to_left else from_left
        from_right = to_left if from_right <= to_right else from_right

        if from_left >= from_right:
            return False, 1
    return True, from_left + 1


@time_this
def time_trial(func, file, y, size):
    func(file, y, size)


# print(main("AOC22_D15_inp0.txt", 10, 20))
answer = main("AOC22_D15_inp.txt", 2000000, 4000000)
print(f'time {time_trial(main,"AOC22_D15_inp.txt", 2000000, 4000000)}  seconds')
print("answer: ", answer)
print("check: ", answer == 11558423398893)
