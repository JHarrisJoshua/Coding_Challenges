import re
from collections import defaultdict


def elephant_walk(file_name):
    adj_list = defaultdict(list)

    with open(file_name, 'r') as infile:
        line: str
        for line in infile:
            flow = int(re.sub("[\sa-zA-Z:,;=]+", '', line))
            print(flow)
            valve = line[7:9]
            nei = re.sub("[\sa-z0-9=;]+", '', line[10:]).split(',')
            print(valve, flow, nei)


print(elephant_walk("AOC22_D16_inp0.txt"))
