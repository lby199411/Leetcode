# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = [None]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.arr.append(root)
            dfs(root.right)
        dfs(root)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index].val

        

    def hasNext(self) -> bool:
        if self.index + 1 < len(self.arr):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()