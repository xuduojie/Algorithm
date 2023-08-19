from typing import List
from queue import Queue


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    ans += 1
                    self.bfs(grid, visited, i, j, m, n)
        return ans

    def bfs(self, grid, visited, sx, sy, m, n):
        q = Queue()
        # 构建方向数组
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        q.put((sx, sy))
        visited[sx][sy] = True
        while not q.empty():
            # 第一步：取队头
            x, y = q.get()
            # 第二步：扩展队头
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                    q.put((nx, ny))
                    visited[nx][ny] = True

# 测试
grid = [
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
solution = Solution()
print(solution.numIslands(grid))
