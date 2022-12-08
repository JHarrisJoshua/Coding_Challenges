from AOC22_D08_B import tree_house_score


def main(file_name):
    with open(file_name, 'r') as infile:
        matrix = [[int(num) for num in line.strip()] for line in infile]
        dp_row = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp_col = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        rows, cols, visible = len(matrix), len(matrix[0]), 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(matrix[i]):
                if i == 0 or j == 0:
                    dp_row[i][j] = dp_col[i][j] = matrix[i][j]
                else:
                    dp_row[i][j] = max(dp_row[i][j-1], matrix[i][j-1])
                    dp_col[i][j] = max(dp_col[i-1][j], matrix[i-1][j])

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i == rows-1 or j==cols-1:
                    dp_row[i][j] = dp_col[i][j] = matrix[i][j]
                else:
                    dp_row[i][j] = min(dp_row[i][j],max(dp_row[i][j+1], matrix[i][j+1]))
                    dp_col[i][j] = min(dp_col[i][j],max(dp_col[i+1][j], matrix[i+1][j]))
                if i in [0,rows-1] or j in [0,rows-1] or matrix[i][j]>min(dp_row[i][j], dp_col[i][j]):
                    visible += 1

    return visible, tree_house_score(matrix)


print('result', main("AOC22_D08_inp.txt"))
# 1787, 440640