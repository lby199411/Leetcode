# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # tree to graph
        self.edge = collections.defaultdict(list)
        def dfs(root):
            if root.left:
                self.edge[root.val].append(root.left.val)
                self.edge[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                self.edge[root.val].append(root.right.val)
                self.edge[root.right.val].append(root.val)
                dfs(root.right)
            return 
        dfs(root)
        visited = set()
        q = deque()
        q.append(start)
        l = 0
        length = len(q)
        while q:
            if length == 0:
                l += 1
                length = len(q)
            num = q.popleft()
            visited.add(num)
            for i in self.edge[num]:
                if i not in visited:
                    q.append(i)
            length -= 1

        return l


            
            
            
        