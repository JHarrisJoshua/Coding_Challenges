def tree_house_score(matrix):
    rows, cols = len(matrix), len(matrix[0])
    best_score = 0
    for row in range(1,rows-1):
        for col in range(1,cols-1):
            score = 1
            for move in [(0,1), (1,0), (0,-1), (-1,0)]:
                r,c = row+move[0], col+move[1]
                counting_trees = 1
                while 0<r<rows-1 and 0<c<cols-1 and matrix[r][c] < matrix[row][col]:
                    counting_trees += 1
                    r, c = r+move[0], c+move[1]
                score *= counting_trees
            best_score = max(best_score, score)
    return best_score
