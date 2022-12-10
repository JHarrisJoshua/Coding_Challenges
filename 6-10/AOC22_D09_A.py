def pin_the_tail_on_the_head(file_name):
    with open(file_name, 'r') as motions:
        head, tail, vis = (0,0), (0,0), {(0,0)}
        moves = {
            'R': lambda steps: (0, steps),
            'L': lambda steps: (0, -steps),
            'U': lambda steps: (steps, 0),
            'D': lambda steps: (-steps, 0)
        }

        for motion in motions:
            motion = list(map(lambda x: int(x) if x.isdigit() else x, motion.strip().split(' ')))
            move = moves[motion[0]](motion[1])
            for i in range(max(abs(move[0]), abs(move[1]))):
                head = (int(head[0]+move[0]/max(1, abs(move[0]))),
                        int(head[1]+move[1]/max(1, abs(move[1]))))
                tail = move_your_tail(head, tail, vis)
        return len(vis)


def move_your_tail(head, tail, vis):
    diffs = (head[0]-tail[0], head[1]-tail[1])
    while abs(diffs[0]) > 1 or abs(diffs[1]) > 1:
        tail = (int(tail[0]+diffs[0]/max(1, abs(diffs[0]))),
                int(tail[1]+diffs[1]/max(1, abs(diffs[1]))))
        vis.add(tail)
        diffs = (head[0] - tail[0], head[1] - tail[1])
    return tail


print(pin_the_tail_on_the_head("AOC22_D09_inp.txt"))

