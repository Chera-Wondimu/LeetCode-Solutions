from heapq import heappush, heappop
from typing import List
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while pq:
            loss, x, y = heappop(pq)
            if loss > dist[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return loss < health
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_loss = loss + grid[nx][ny]
                    if new_loss < dist[nx][ny]:
                        dist[nx][ny] = new_loss
                        heappush(pq, (new_loss, nx, ny))
        return False