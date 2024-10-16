class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ret = ''
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)
        i = 0
        while i < a + b + c:
            i += 1
            occur, s = heapq.heappop(heap)
            if len(ret) < 2 or s != ret[-1] or s != ret[-2]:
                ret += s
                heapq.heappush(heap, (occur + 1, s))
            else:
                occur2, s2 = heapq.heappop(heap)
                if occur2 == 0:
                    break
                else:
                    ret += s2
                    heapq.heappush(heap, (occur2 + 1, s2))
                heapq.heappush(heap, (occur, s))
        return ret

            


