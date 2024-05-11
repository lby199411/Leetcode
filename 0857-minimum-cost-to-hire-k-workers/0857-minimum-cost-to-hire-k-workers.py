class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # let total wage to be small -> let quality small and let wage/quality small 
        ratio = [(wage[i]/quality[i], quality[i]) for i in range(len(wage))]
        ratio.sort()
        max_heap = []
        quality_sum = 0
        max_ratio = 0
        ret = 0
        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])
        ret = max_ratio*quality_sum
        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ratio[i][1])
            ret = min(ret, max_ratio * quality_sum)
        return ret
