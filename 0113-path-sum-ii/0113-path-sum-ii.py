# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # dfs
        ret = []
        def dfs(root, path, summation):
            path.append(root.val)
            summation += root.val
            if not root.left and not root.right:
                if summation == targetSum:
                    ret.append(path[:])
                return
            if root.left:
                dfs(root.left, path[:], summation)
            if root.right:
                dfs(root.right, path[:], summation)
        dfs(root, [], 0)
        return ret
