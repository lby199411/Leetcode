class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        #screening edges
        if len(edges) == 0:
            return 0
        dic = collections.defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        n = len(edges) + 1
        # BFS
        def bfs(start, n, dic):
            visited = [False]*n
            q = collections.deque()
            q.append(start)
            dia = 0
            count = 1
            while q:
                if count == 0:
                    dia += 1
                    count = len(q)
                tem = q.popleft()
                visited[tem] = True
                for node in dic[tem]:
                    if visited[node] == False:
                        q.append(node)
                count -= 1
            return tem, dia
        
        for node in dic:
            if len(dic[node]) == 1:
                start = node
                break
        tem, _ = bfs(start, n, dic)
        _, dia = bfs(tem, n, dic)

        return dia
            