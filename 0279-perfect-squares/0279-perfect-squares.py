class Solution:
    def numSquares(self, n: int) -> int:
        dp =[n for _ in range(n+1)]
        square_num = [i*i for i in range(1,int(math.sqrt(n))+1)]
        dp[0] = 0      
        
        for i in range(1,n+1):
            for square in square_num:
                if i< square:
                    break
                dp[i] = min(dp[i],dp[i-square]+1)

        return dp[n]