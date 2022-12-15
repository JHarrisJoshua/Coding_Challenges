def get_marker(file_name, distinct_chars):
    with open(file_name, 'rb') as infile:
        marker = distinct_chars
        while True:
            chars = set(infile.read(distinct_chars))
            if len(chars) == distinct_chars:
                return marker
            else:
                marker += 1
                infile.seek(1-distinct_chars, 1)


print(get_marker("AOC22_D06_inp.txt", 4))
print(get_marker("AOC22_D06_inp.txt", 14))
