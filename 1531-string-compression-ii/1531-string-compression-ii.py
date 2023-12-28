class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # dp
        getlen = lambda x: x if x <= 1 else 2 + int(math.log10(x))
        @cache
        def recursive(i, k):
            if i < 0:
                return 0
            if k:
                ans = recursive(i - 1, k - 1)
            else:
                ans = math.inf
            
            freq = 0
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    freq += 1
                elif k == 0:
                    return ans
                else:
                    k -= 1
                ans = min(ans, recursive(j - 1, k) + getlen(freq))
            
            return ans
        return recursive(len(s) - 1, k)
            

