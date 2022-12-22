from collections import OrderedDict


def get_marker(file_name, distinct_chars):
    with open(file_name, 'r') as infile:
        fifo_dict, marker = OrderedDict(), 0

        while len(fifo_dict) < distinct_chars:
            char, marker = infile.read(1), marker + 1
            while char in fifo_dict:
                fifo_dict.popitem(last=False)
            fifo_dict[char] = 1
            if len(fifo_dict) == distinct_chars:
                return marker


print(get_marker("AOC22_D06_inp.txt", 4))
print(get_marker("AOC22_D06_inp.txt", 14))
