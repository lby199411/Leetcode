class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove)]
        dp[0][startRow][startColumn] = 1

        for move in range(1, maxMove):
            for row in range(m):
                for col in range(n):
                    for a, b in [[1,0], [-1,0], [0,1], [0,-1]]:
                        prev_row, prev_col = row + a, col + b
                        if prev_row > -1 and prev_row < m and prev_col > -1 and prev_col <n:
                            dp[move][row][col] += dp[move - 1][prev_row][prev_col]
        self.ret = 0
        for move in range(maxMove):
            for row in range(m):
                for col in range(n):       
                    if row == 0:
                        self.ret += dp[move][row][col]
                    if row == m - 1:
                        self.ret += dp[move][row][col]
                    if col == 0 :
                        self.ret += dp[move][row][col]
                    if col == n - 1:
                        self.ret += dp[move][row][col]
        return self.ret % (10**9 + 7)
                
                
                
