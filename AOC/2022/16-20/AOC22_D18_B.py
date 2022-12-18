from collections import deque


def the_floor_is_lava(file_name):
    lava, surface_area, grid_size = set(), 0, 0
    with open(file_name, 'r') as lava_droplets:
        for droplet in lava_droplets:
            location = tuple(map(int, droplet.split(',')))
            grid_size = max(grid_size, max(location))
            lava.add(location)

    water = flood_fill(lava, grid_size+1)
    for droplet in lava:
        x, y, z = droplet
        for x2,y2,z2 in [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z),
                                               (x,y,z+1), (x,y,z-1)]:
            if (x2,y2,z2) in water:
                surface_area += 1
    return surface_area


def flood_fill(lava, size):
    water, flood = {(-1,-1,-1)}, deque([(-1,-1,-1)])
    while flood:
        x,y,z = flood.popleft()
        for x2,y2,z2 in [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z),
                                               (x,y,z+1), (x,y,z-1)]:
            if not all([-1<=x2<=size,-1<=y2<=size,-1<=z2<=size]):
                continue
            if (x2,y2,z2) in lava or (x2,y2,z2) in water:
                continue
            water.add((x2,y2,z2)), flood.append((x2,y2,z2))
    return water


print(the_floor_is_lava("AOC22_D18_inp.txt"))
# 1996 too low, someone else's answer
