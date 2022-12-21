from heapq import heappush, heappop
import re


def main(file_name, turns):
    blueprints = dict()
    factory = ['ge', 'ob', 'cl', 'or', 'None']
    result = {'tot': 0, 'blueprints': dict()}
    with open(file_name, 'r') as infile:
        for line in infile:
            line = list(map(int, re.findall(r'\b\d+\b', line.strip())))
            blueprints[line[0]] = dict()
            blueprints[line[0]]['or'] = {'or': line[1]}
            blueprints[line[0]]['cl'] = {'or': line[2]}
            blueprints[line[0]]['ob'] = {'or': line[3], 'cl':line[4]}
            blueprints[line[0]]['ge'] = {'or': line[5], 'ob':line[6]}

    for blueprint, requirements in blueprints.items():
        robots = {'or': 1, 'cl': 0, 'ob': 0, 'ge': 0}
        inventory, max_ge = {'or': 0, 'cl': 0, 'ob': 0, 'ge': 0}, 0
        heap = [(1, 0, 0, robots, inventory)]

        max_turn, i = 1, 1
        while heap:
            turn, order, idx, robots, inventory = heappop(heap)
            max_ge = max(max_ge, inventory['ge'] + robots['ge'])
            if turn > max_turn:
                max_turn = turn
                if heap and len(heap) > 500:
                    heap = clean_heap(heap)
            for station in factory:
                new_inv, new_robots = dict(inventory), dict(robots)
                if station == 'None':
                    for robot, number in robots.items():
                        new_inv[robot] += number
                    if turn < turns:
                        order = (-new_inv['ge'], -new_robots['ge'],
                                 -new_robots['ob'], -new_inv['ob'],
                                 -new_robots['cl'], -new_inv['cl'],
                                 -new_robots['or'])
                        heappush(heap, (turn+1, order, i, new_robots, new_inv))
                        i+= 1
                else:
                    requirement = requirements[station]
                    build = True
                    for ore, needed in requirement.items():
                        if needed > inventory[ore]:
                            build = False
                            break
                        new_inv[ore] -= needed
                    if build and turn < turns:
                        for robot, number in robots.items():
                            new_inv[robot] += number
                        new_robots[station] += 1
                        order = (-new_inv['ge'], -new_robots['ge'],
                                 -new_robots['ob'], -new_inv['ob'],
                                 -new_robots['cl'], -new_inv['cl'],
                                 -new_robots['or'])
                        heappush(heap, (turn+1, order, i, new_robots, new_inv))
                        i += 1

        result['tot'] += max_ge * blueprint
        result['blueprints'][blueprint] = max_ge
    return result


def clean_heap(old_heap):
    new_heap = []
    for _ in range(500):
        heappush(new_heap, heappop(old_heap))
    return new_heap


if __name__=='__main__':
    print(main("AOC22_D19_inp.txt", 24))
