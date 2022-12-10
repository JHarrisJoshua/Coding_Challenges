def pin_the_tail_on_the_head(file_name, num_knots):
    with open(file_name, 'r') as motions:
        knots, vis = [(0,0)] * num_knots, {(0,0)}
        moves = {
            'R': lambda steps: (0, steps),
            'L': lambda steps: (0, -steps),
            'U': lambda steps: (steps, 0),
            'D': lambda steps: (-steps, 0)
        }

        for motion in motions:
            motion = list(map(lambda x: int(x) if x.isdigit() else x, motion.strip().split(' ')))
            move = moves[motion[0]](motion[1])
            for _ in range(max(abs(move[0]), abs(move[1]))):
                knots[0] = (int(knots[0][0]+move[0]/max(1, abs(move[0]))),
                            int(knots[0][1]+move[1]/max(1, abs(move[1]))))
                for k in range(1, num_knots):
                    knots[k] = move_your_knots(knots[k], knots[k-1], vis, (k == num_knots-1))
        return len(vis)


def move_your_knots(curr, prev, vis, is_tail):
    diffs = (prev[0]-curr[0], prev[1]-curr[1])
    while abs(diffs[0]) > 1 or abs(diffs[1]) > 1:
        curr = (int(curr[0]+diffs[0]/max(1, abs(diffs[0]))),
                int(curr[1]+diffs[1]/max(1, abs(diffs[1]))))
        diffs = (prev[0] - curr[0], prev[1] - curr[1])
        if is_tail:
            vis.add(curr)
    return curr


print(pin_the_tail_on_the_head("AOC22_D09_inp.txt", 2))
print(pin_the_tail_on_the_head("AOC22_D09_inp.txt", 10))

