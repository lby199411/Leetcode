class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        def getsuittime(arr1, arr2):
            arr1.sort()
            arr2.sort()
            i, j =0 , 0
            ret = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i][0] > arr2[j][1]:
                    j += 1
                elif arr2[j][0] > arr1[i][1]:
                    i += 1
                else:
                    ret.append([max(arr1[i][0], arr2[j][0]), min(arr1[i][1], arr2[j][1])])
                    if arr1[i][1] > arr2[j][1]:
                        j += 1
                    elif arr1[i][1] < arr2[j][1]:
                        i += 1
                    else:
                        i += 1
                        j += 1
            return ret
        region = getsuittime(slots1, slots2)
        for time in region:
            if time[1] - time[0] >= duration:
                return [time[0], time[0] + duration]
        return []

