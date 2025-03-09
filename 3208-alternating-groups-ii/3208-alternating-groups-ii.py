class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ret = 0
        colors = colors + colors[:k - 1]
        tem = 1
        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                tem += 1
            else:
                if tem >=k:
                    ret += tem - k + 1
                tem = 1
        if tem >=k:
            ret += tem - k + 1     
        return ret
                