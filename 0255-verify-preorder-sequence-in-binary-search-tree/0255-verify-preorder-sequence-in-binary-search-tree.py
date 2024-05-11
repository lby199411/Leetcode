class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        #print(arr)
        stack = []
        min_val = -math.inf
        for val in preorder:
            while stack and stack[-1] < val:
                min_val = stack[-1]
                stack.pop()
            if val < min_val:
                return False
            stack.append(val)
        return True
                




