class Solution:
    def minSwaps(self, s: str) -> int:
        val = 0
        count = 0
        for char in s:
            if char == ']':
                val += 1
            else:
                val -= 1
            count = max(count, val)
        return math.ceil(count/2)