class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        presum = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    presum[i][j] = img[i][j]
                elif i == 0:
                    presum[i][j] = presum[i][j-1]  + img[i][j]
                elif j == 0:
                    presum[i][j] = presum[i-1][j]  + img[i][j]
                else:
                    presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + img[i][j]
        ret = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                min_row, max_row = max(row - 1, 0), min(row + 1, rows - 1)
                min_col, max_col = max(col - 1, 0), min(col + 1, cols - 1)
                if min_row == 0 and min_col == 0:
                    sumarea = presum[max_row][max_col]
                elif min_row == 0:
                    sumarea = presum[max_row][max_col] - presum[max_row][min_col - 1]
                elif min_col == 0:
                    sumarea = presum[max_row][max_col] - presum[min_row - 1][max_col]
                else:
                    sumarea = presum[max_row][max_col] - presum[max_row][min_col - 1] - presum[min_row - 1][max_col] + presum[min_row - 1][min_col - 1]
                ret[row][col] = sumarea//((max_row - min_row + 1)*(max_col - min_col + 1))

        return ret
        