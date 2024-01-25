class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] == 1:
            return math.ceil(nums.count(1)/2)
        while True:
            min_mod, index = math.inf, 0
            for i in range(len(nums)):
                mod = nums[i] % nums[0]
                if mod>0 and mod < min_mod:
                    min_mod = mod
                    index = i
            if min_mod == 1:
                return 1
            elif min_mod == math.inf:
                return math.ceil(nums.count(nums[0])/2)
            else:
                nums[0] = min_mod
                nums.pop(i)


        