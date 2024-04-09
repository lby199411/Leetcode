# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        if not root:
            return []
        tem, ret = [], []
        q = collections.deque()
        q.append(root)
        count = 1
        while q:
            node = q.popleft()
            tem.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            count -= 1
            if count == 0:
                count = len(q)
                ret.append(tem)
                tem = []

        return ret[::-1]


