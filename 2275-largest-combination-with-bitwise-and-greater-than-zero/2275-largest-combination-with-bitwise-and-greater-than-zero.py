class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        l = len(candidates)
        max_length = len(bin(l)) - 2
        count = [0]*max_length
        for val in candidates:
            s = bin(val)[2:]
            s = (l -len(s))*'0' + s
            for i in range(max_length):
                if s[i] == '1':
                    count[i] += 1
        return max(count)
            