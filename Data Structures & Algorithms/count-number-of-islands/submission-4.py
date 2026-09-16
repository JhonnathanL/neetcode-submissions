from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            visited.add((r, c))

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr,nc) 
                    not in visited):
                        queue.append((nr,nc))
                        visited.add((nr,nc))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands+= 1
        
        return islands

