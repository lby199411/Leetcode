class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = collections.Counter(word)
        l = [counter[key] for key in counter]
        l.sort()
        l = l + [0]*(26 - len(l))
        ret = 0
        for i in range(26):
            if i < 8:
                ret += l[i]*1
            elif i < 16:
                ret += l[i]*2
            elif i < 24:
                ret += l[i]*3
            else:
                ret += l[i]*4
        return ret

