class Solution:
    def minChanges(self, s: str) -> int:
        ret = 0
        for i in range(len(s)//2):
            if s[2*i] != s[2*i + 1]:
                ret += 1
        return ret

