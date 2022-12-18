from AOC22_D08_B import tree_house_score


def tree_house_hunters(file_name):
    with open(file_name, 'r') as infile:
        trees = [[int(num) for num in line.strip()] for line in infile]
        rows, cols, visible = len(trees), len(trees[0]), 0
        dp_row = [[0 for _ in range(rows)] for _ in range(cols)]
        dp_col = [[0 for _ in range(rows)] for _ in range(cols)]

        for i, row in enumerate(trees):
            for j, val in enumerate(trees[i]):
                if i == 0 or j == 0:
                    dp_row[i][j] = dp_col[i][j] = trees[i][j]
                else:
                    dp_row[i][j] = max(dp_row[i][j-1], trees[i][j-1])
                    dp_col[i][j] = max(dp_col[i-1][j], trees[i-1][j])

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i == rows-1 or j==cols-1:
                    dp_row[i][j] = dp_col[i][j] = trees[i][j]
                else:
                    dp_row[i][j] = min(dp_row[i][j],max(dp_row[i][j+1], trees[i][j+1]))
                    dp_col[i][j] = min(dp_col[i][j],max(dp_col[i+1][j], trees[i+1][j]))
                if i in [0,rows-1] or j in [0,rows-1] or trees[i][j]>min(dp_row[i][j], dp_col[i][j]):
                    visible += 1

    return visible, tree_house_score(trees)


print('result', tree_house_hunters("AOC22_D08_inp.txt"))
# 1787, 440640
