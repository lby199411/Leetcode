class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        vals = [dic[key] for key in dic]
        vals.sort(reverse = True)
        max_val = vals[0]
        ret = 0
        for val in vals:
            if val == max_val:
                ret += max_val
            else:
                break
        return ret

        