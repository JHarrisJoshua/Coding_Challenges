def main(file_name):
    with open(file_name, 'r') as infile:
        paper = ribbon = 0
        for line in infile:
            l, w, h = [int(x) for x in line.strip().split("x")]
            paper += 2 * (l*w + l*h + w*h) + min(l*w,l*h,w*h)
            ribbon += 2 * min(l+w,l+h,w+h) + l*w*h
    return paper, ribbon


print(main("AOC15_D02_inp.txt"))
