# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.ret = False
        target = []
        while head:
            target.append(head.val)
            head = head.next
        def dfs(root, path):
            if not root:
                if len(path) >= len(target):
                    for i in range(len(path) - len(target) + 1):
                        if target == path[i: i + len(target)]:
                            self.ret = True
                return
            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return self.ret
