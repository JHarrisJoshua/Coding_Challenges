from ast import literal_eval
from math import inf
from collections import deque
from sys import maxsize


class LineSorter(list):
    def __lt__(line1, line2):
        if line1 in [[3]] or line2 in [[3]]:
            print("test")
        # print(f" line 1: {line1}, line2:  {line2}")
        is_lt = compare_sort(line1[::], line2[::])

        # print(is_lt)
        # print(f" line 1: {line1}, line2:  {line2}")
        return \
            is_lt


def main(file_name):
    result = []
    sorted_lines = [[[6]], [[2]]]
    with open(file_name, 'r') as infile:
        lines = [line.strip() for line in infile if line != '\n']
        lines = deque([literal_eval(line) for line in lines])
        # print(lines)
        i = 1
        # if i in [4,5,6,7]:
        #     print("test")
        while lines:
            line_1 = lines.popleft()
            line_2 = lines.popleft()
            sorted_lines.append(line_1), sorted_lines.append(line_2)
            print("1: ", line_1, "2: ", line_2)
            compare(line_1, line_2, result, i)
            check_tot = 0
            check = compare_sort(line_1, line_2)
            if check:
                check_tot += 1
            print(f"i: {i} -> ", check)
            i += 1
    # print('-----unsorted down')
    # print(sorted_lines)
    # print('-----unsorted up')
    for i, row in enumerate(sorted_lines):
        # print('-----uncoverted')
        # print(sorted_lines[i])
        sorted_lines[i] = line_coverter(row)
        # print('-----converted')
        # print(sorted_lines[i])

    sorted_lines.sort(key=LineSorter)
    x, y = sorted_lines.index([2]), sorted_lines.index([6])
    return result, sum(result), sorted_lines, (x+1)*(y+1)


def line_coverter(line_1, level=-maxsize, result=None):
    if result is None:
        result = []
    if len(line_1) == 0:
        result.append(level)

    for i, item in enumerate(line_1):
        if type(item) != list:
            result.append(item)
        else:
            result.extend(line_coverter(item, level+1))
    return result


def compare_sort(line_1, line_2, j=0):
    # print("line_1", line_1, "line_2", line_2, "res", result, i, j)
    while j < len(line_1) or j < len(line_2):
        if j >= len(line_1):
            return True
        elif j >= len(line_2):
            return False

        if type(line_1[j]) in (int, float) and type(line_2[j]) in (int, float):
            if line_1[j] > line_2[j]:
                return False
            if line_1[j] < line_2[j]:
                return True
            j += 1
        elif type(line_1[j]) == list or type(line_2[j]) == list:
            cmp_1 = line_1[j] if type(line_1[j]) == list else [line_1[j]]
            cmp_2 = line_2[j] if type(line_2[j]) == list else [line_2[j]]
            if compare_sort(cmp_1, cmp_2):
                return True
            else:
                j += 1
        else:
            print("test this")
            # print(line_1[j])
            # print(line_2[j])
    return True

# def compare_sort(line_1, line_2, j=0):
#     # print("line_1", line_1, "line_2", line_2, "res", result, i, j)
#     while j < len(line_1) or j < len(line_2):
#         if j >= len(line_1):
#
#             return True
#         elif j >= len(line_2):
#             return False
#
#         if type(line_1[j]) == int and type(line_2[j]) == int:
#             if line_1[j] > line_2[j]:
#                 return False
#             if line_1[j] < line_2[j]:
#
#                 return True
#             j += 1
#         elif type(line_1[j]) == list or type(line_2[j]) == list:
#             cmp_1 = line_1[j] if type(line_1[j]) == list else [line_1[j]]
#             cmp_2 = line_2[j] if type(line_2[j]) == list else [line_2[j]]
#             if not compare_sort(cmp_1, cmp_2):
#                 return False
#             else:
#                 j += 1
#         else:
#             print("test this")
#             print(line_1[j])
#             print(line_2[j])
#     return True


def compare(line_1, line_2, result, i, j=0):
    # print("line_1", line_1, "line_2", line_2, "res", result, i, j)
    while j < len(line_1) or j < len(line_2):
        if j >= len(line_1):
            result.append(i)
            return False
        elif j >= len(line_2):
            return False

        if type(line_1[j]) in (int, float) and type(line_2[j]) in (int,float):
            if line_1[j] > line_2[j]:
                return False
            if line_1[j] < line_2[j]:
                result.append(i)
                return False
            j += 1
        elif type(line_1[j]) == list or type(line_2[j]) == list:
            cmp_1 = line_1[j] if type(line_1[j]) == list else [line_1[j]]
            cmp_2 = line_2[j] if type(line_2[j]) == list else [line_2[j]]
            if not compare(cmp_1, cmp_2, result, i):
                return False
            else:
                j += 1
        else:
            print("test this")
            # print(line_1[j])
            # print(line_2[j])
    return True

print(type(inf))

part_1_arr, part_1_sum, part_2_arr, part_2_res = main("AOC22_D13_inp.txt")
print("Part 1: ", part_1_arr, part_1_sum)

# print('-----')
#
print(part_2_res)

# 5196  22134

