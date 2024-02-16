class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = collections.Counter(arr)
        lst = [(key, dic[key]) for key in dic]
        lst.sort(key = lambda x: x[1])
        i = 0
        while i < len(lst):
            if k >= lst[i][1]:
                k -= lst[i][1]
                i += 1
            else:
                break
        return len(lst) - i
