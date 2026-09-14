from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        max_area = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            area = 1

            directions = [
                [1,0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited 
                    and grid[nr][nc] == 1):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(bfs(i,j), max_area)

        return max_area