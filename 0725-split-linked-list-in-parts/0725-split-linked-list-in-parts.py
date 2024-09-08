# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy.next
        length = 0
        while curr:
            length += 1
            curr = curr.next
        avg = length//k
        res = length%k
        arr = [avg] * k
        for i in range(res):
            arr[i] += 1
        node = head
        ret = []
        for i in range(k):
            if arr[i] == 0:
                ret.append(None)
            else:
                ret.append(node)
                while arr[i] > 1:
                    node = node.next
                    arr[i] -= 1
                tem = node.next
                node.next = None
                node = tem
        return ret
                




        

