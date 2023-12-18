class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ret = 0
        pre_height = 0

        while i < j:
            curr_height = min(height[i], height[j])
            if curr_height > pre_height:
                pre_height = curr_height
            else:
                ret += pre_height - curr_height
            if curr_height == height[i]:
                i += 1
            else:
                j -= 1
                
        return ret

