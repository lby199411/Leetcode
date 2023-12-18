class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # union and find
        m ,n = len(grid) , len(grid[0])
        par = [[ None for _ in range(n)] for _ in range(m)]
        visited = [[ False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    par[i][j] = [i, j]
        print(par)
        def dfs(row, col, visited, par):
            visited[row][col] = True
            for a, b in [[1,0], [-1,0], [0,1], [0,-1]]:
                new_row, new_col = row + a, col + b
                if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and visited[new_row][new_col] == False and par[new_row][new_col] != None:
                    par[new_row][new_col] = par[row][col]
                    dfs(new_row, new_col, visited, par)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == False:
                    dfs(i, j, visited, par)
        ret = set()
        for i in range(m):
            for j in range(n):
                if par[i][j] != None and tuple(par[i][j]) not in ret:
                    ret.add(tuple(par[i][j]))
        return len(ret)
            