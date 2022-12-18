def the_floor_is_lava(file_name):
    droplets, surface_area = set(), 0
    with open(file_name, 'r') as lava:
        for droplet in lava:
            droplets.add(tuple(map(int, droplet.split(','))))

    for droplet in droplets:
        x, y, z = droplet
        for x2, y2, z2 in [(x + 1, y, z), (x - 1, y, z),
                           (x, y + 1, z), (x, y - 1, z),
                           (x, y, z + 1), (x, y, z - 1)]:
            if (x2, y2, z2) not in droplets:
                surface_area += 1
    return surface_area


print(the_floor_is_lava("AOC22_D18_inp.txt"))
