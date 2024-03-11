class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ret = ['']*len(arr)
        for i in range(len(arr)):
            s = arr[i]
            l = 1
            while l <= len(s):
                for j in range(len(s) + 1 - l):
                    tem = s[j:j + l]
                    flag = True
                    for k in range(len(arr)):
                        if k != i and tem in arr[k]:
                            flag = False
                            break
                    if flag :
                        if ret[i] == '':
                            ret[i] = tem
                        else:
                            ret[i] = min(ret[i], tem)

                if ret[i] != '':
                    break
                l += 1
        return ret
                        
            