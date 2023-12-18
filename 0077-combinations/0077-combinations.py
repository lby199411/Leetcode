class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret = []
        def bt(index, arr, n, k):
            if len(arr) == k:
                self.ret.append(arr[:])
                return
            if index == n:
                return
            bt(index + 1, arr, n, k)
            arr.append(index + 1)
            bt(index + 1, arr, n, k)
            arr.pop()

        bt(0, [], n, k)
        return self.ret
