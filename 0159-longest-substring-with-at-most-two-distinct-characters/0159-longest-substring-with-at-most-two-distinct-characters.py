class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        ret = 0
        l, r =0, 0
        while r < len(s):
            if len(dic) > 2:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            else:
                if s[r] in dic:
                    dic[s[r]] += 1
                else:
                    dic[s[r]] = 1
                if len(dic) <= 2:
                    ret = max(ret, r - l + 1)
                r += 1
        return ret




