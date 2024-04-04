class Solution:
    def maxDepth(self, s: str) -> int:
        layer, ret = 0, 0
        for letter in s:
            if letter == '(':
                layer += 1
            elif letter == ')':
                layer -= 1
            ret = max(ret, layer)
        return ret
            