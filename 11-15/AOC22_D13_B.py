from ast import literal_eval
from collections import deque


class LineSorter(str):
    def __lt__(line1, line2):
        compare_sort(line1, line2)
        return compare_sort(line1, line2)


def main(file_name):
    result = []
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
            print("1: ", line_1, "2: ", line_2)
            check = compare(line_1, line_2, result, i)
            print(f"i: {i} -> ", check)
            i += 1
    return result, sum(result)


def compare_sort(line_1, line_2, j=0):
    # print("line_1", line_1, "line_2", line_2, "res", result, i, j)
    while j < len(line_1) or j < len(line_2):
        if j >= len(line_1):
            return True
        elif j >= len(line_2):
            return False

        if type(line_1[j]) == int and type(line_2[j]) == int:
            if line_1[j] > line_2[j]:
                return False
            if line_1[j] < line_2[j]:
                return True
            j += 1
        elif type(line_1[j]) == list and type(line_2[j]) == list:
            if not compare(line_1[j], line_2[j], result, i):
                return False
            else:
                j += 1
        else:
            line_1[j] = line_1[j] if type(line_1[j]) == list else [line_1[j]]
            line_2[j] = line_2[j] if type(line_2[j]) == list else [line_2[j]]
    return True


def compare(line_1, line_2, result, i, j=0):
    # print("line_1", line_1, "line_2", line_2, "res", result, i, j)
    while j < len(line_1) or j < len(line_2):
        if j >= len(line_1):
            result.append(i)
            return False
        elif j >= len(line_2):
            return False

        if type(line_1[j]) == int and type(line_2[j]) == int:
            if line_1[j] > line_2[j]:
                return False
            if line_1[j] < line_2[j]:
                result.append(i)
                return False
            j += 1
        elif type(line_1[j]) == list and type(line_2[j]) == list:
            if not compare(line_1[j], line_2[j], result, i):
                return False
            else:
                j += 1
        else:
            line_1[j] = line_1[j] if type(line_1[j]) == list else [line_1[j]]
            line_2[j] = line_2[j] if type(line_2[j]) == list else [line_2[j]]
    return True


print(main("AOC22_D13_inp0.txt"))
