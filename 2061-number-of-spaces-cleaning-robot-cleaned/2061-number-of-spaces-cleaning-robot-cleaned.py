class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        # (x, y, d) : d is the parameter to store the facing direction at pos (x, y)
        # loop would end if (x, y, f) appears twice
        # direction 0: right, 1: down 2: left 3: up
        m, n = len(room), len(room[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited, status = set(), set()
        curr = (0, 0, 0)
        while curr not in status:
            status.add(curr)
            x, y, d = curr
            if (x, y) not in visited:
                visited.add((x, y))
            flag, loop = True, 4
            while flag and loop:
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and room[nx][ny] == 0:
                    flag = False
                else:
                    loop -= 1
                    d = (d + 1)%4
            if loop == 0:
                return len(visited)
            curr = (nx, ny, d)
        return len(visited)
                


            


        