class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff_row = []
        diff_col = []
        diff = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in grid:
            tem = 0
            for col in row:
                if col == 1:
                    tem += 1
                else:
                    tem -= 1
            diff_row.append(tem)
        for i in range(len(grid[0])):
            tem = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    tem += 1
                else:
                    tem -= 1
            diff_col.append(tem)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = diff_row[i] + diff_col[j]
        return diff


        
