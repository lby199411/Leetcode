class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        arr = []
        curr = 0
        target = 2**maximumBit - 1
        ret = []
        for val in nums:
            curr = curr ^ val
            arr.append(curr)
        for val in arr:
            ret.append(target ^ val)
        return ret[::-1]