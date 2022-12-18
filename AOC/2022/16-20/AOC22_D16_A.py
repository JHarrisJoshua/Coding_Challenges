from collections import defaultdict, deque
from heapq import heappush, heappop
import heapq
import re
import pprint


def elephant_walk(file_name, source="AA", mins=30):
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
    heap = [(step, tot_flow, rate, source, opened)]

    max_step = 0
    steps = defaultdict(dict)
    steps[max_step], steps[30] = 0, 0

    while heap:
        if len(heap) > 2000:
            heap = clean_up_heap(heap)

        step, tot_flow, rate, valve, opened = heappop(heap)
        if step > max_step:
            max_step = step
            print(max_step)
            steps[max_step] = tot_flow
        steps[max_step] = max(steps[max_step], -tot_flow)
        if step == 30:
            continue
        for nei in valves[valve]['nei']:
            flow, new_rate = valves[nei]['flow'], rate
            new_step, new_opened = step + 1, opened
            new_tot = tot_flow + rate

            for idx in range(2):
                if idx == 1 and nei not in opened and flow >= 1:
                    new_rate, new_step = rate - flow, new_step + 1
                    new_tot, new_opened = new_tot + new_rate, new_opened|{nei}
                elif idx == 1:
                    continue
                if new_step <= 30:
                    heappush(heap, (new_step, new_tot, new_rate, nei, new_opened))
    return steps[30]




def flight_of_the_elephants():
    pass

def clean_up_heap(heap):
    sorted_heap = deque(sorted(heap, key=lambda x: x[1]))
    new_heap = []
    for _ in range(1000):
        heappush(new_heap, sorted_heap.popleft())
    return new_heap


if __name__ == '__main__':
    print(elephant_walk("AOC22_D16_inp.txt"))
