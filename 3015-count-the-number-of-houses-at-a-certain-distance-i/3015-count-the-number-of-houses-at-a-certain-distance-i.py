class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # bfs
        dic = collections.defaultdict(list)
        for i in range(1, n):
            dic[i].append(i + 1)
            dic[i + 1].append(i)
        dic[x].append(y)
        dic[y].append(x)
        ret = [0]*n
        for i in range(1, n+1):
            q = collections.deque()
            q.append(i)
            dis, count = 0, 1
            visited = set()
            visited.add(i)
            while q:
                if count == 0:
                    dis += 1
                    count = len(q)
                node = q.popleft()
                if dis > 0:
                    ret[dis-1] += 1
                for val in dic[node]:
                    if val not in visited:
                        q.append(val)
                        visited.add(val)
                count -= 1
        return ret



