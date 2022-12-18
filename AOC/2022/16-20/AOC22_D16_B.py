from collections import defaultdict, deque
from heapq import heappush, heappop
import heapq
import re
import pprint


def elephant_walk(file_name, source="AA", mins=26):
    valves = defaultdict(dict)

    with open(file_name, 'r') as infile:
        line: str
        for line in infile:
            flow = int(re.sub(r"[\sa-zA-Z:,;=]+", '', line))
            nei = set(re.sub(r"[\sa-z0-9=;]+", '', line[10:]).split(','))
            valve, attrib, vals = line[6:8], ['flow', 'nei','closed'], [flow, nei, True]
            print(f"valve: {valve}, flow: {flow}, nei: {nei}")
            valves[valve] = dict(zip(attrib, vals))

    pp = pprint.PrettyPrinter()
    pp.pprint(valves)
    pressure = map_out_biodome_tunnels(valves, source, mins)
    print(pressure)
    return pressure


def map_out_biodome_tunnels(valves, source, mins):
    """ Just saving some elephants over here."""
    step, rate, tot_flow, opened = 1, 0, 0, set()
    heap = [(step, tot_flow, rate, source, source, opened)]

    max_step = 0
    steps = defaultdict(dict)
    steps[max_step], steps[26] = 0, 0

    while heap:
        if len(heap) > 2000:
            heap = clean_up_heap(heap)

        step, tot_flow, rate, valve, ele, opened = heappop(heap)
        flow = valves[valve]['flow']
        flow2 = valves[ele]['flow']
        if step > max_step:
            max_step = step
            print(max_step)
            steps[max_step] = tot_flow
        steps[max_step] = max(steps[max_step], -tot_flow)
        if step == mins:
            continue
        for nei in valves[valve]['nei']:
            for idx in range(2):
                for nei2 in valves[ele]['nei']:
                    for jdx in range(2):
                        if step > 26:
                            continue
                        if idx == 0 and jdx == 0:
                            heappush(heap, (step+1, tot_flow+rate, rate, nei, nei2, opened))
                        elif idx == 0 and jdx == 1:
                            if ele in opened or flow2 == 0:
                                continue
                            heappush(heap, (step+1, tot_flow+rate-flow2, rate-flow2, nei, ele, opened|{ele}))
                        elif idx == 1 and jdx == 0:
                            if valve in opened or flow == 0:
                                continue
                            heappush(heap, (step+1, tot_flow+rate-flow, rate-flow, valve, nei2, opened|{valve}))
                        else:
                            if valve in opened or flow == 0 or ele in opened or flow2 == 0:
                                continue
                            heappush(heap, (step+1, tot_flow+rate-flow-flow2, rate-flow-flow2,
                                            valve, ele, opened|{valve}|{ele}))
    return steps[26]


def flight_of_the_elephants():
    pass


def clean_up_heap(heap):
    sorted_heap = deque(sorted(heap, key=lambda x: x[1]))
    new_heap = []
    for _ in range(1000):
        heappush(new_heap, sorted_heap.popleft())
    return new_heap


if __name__ == '__main__':
    print(elephant_walk("AOC22_D16_inp0.txt"))
