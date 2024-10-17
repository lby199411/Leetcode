class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        lst = [s[i] for i in range(len(s))]
        dic = collections.defaultdict(set)
        for i, val in enumerate(s):
            dic[val].add(i)
        for i in range(len((s))):
            max_val = max([ key for key in dic])
            if s[i] != max_val:
                arr = list(dic[max_val])
                pos = int(max(arr))
                lst[i], lst[pos] = lst[pos], lst[i]
                s = ''.join(lst)
                break
            dic[max_val].remove(i)
            if not dic[max_val]:
                del dic[max_val]
        return int(s)
        



        

        