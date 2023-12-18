class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            B, A = nums1, nums2
        total = (len(nums1) + len(nums2))//2
        start, end = 0, len(A) - 1
        if start > end:
            return B[len(B)//2] if len(B)%2 else (B[len(B)//2] + B[len(B)//2-1])/2
        while True:
            mid = (start + end)//2
            mid_B = total - mid - 2
            Aleft = A[mid] if mid >=0 else -math.inf
            Aright = A[mid+1] if mid+1 < len(A) else math.inf
            Bleft = B[mid_B] if mid_B >=0 else -math.inf
            Bright = B[mid_B+1] if mid_B+1 < len(B) else math.inf            
            if Aleft <= Bright and Bleft <= Aright:
                if (len(nums1) + len(nums2))%2:
                    return min(Bright,Aright)
                else:
                    return (min(Bright,Aright) + max(Bleft,Aleft))/2
            elif Bleft >= Aright:
                start = mid + 1
            else:
                end = mid - 1
        
