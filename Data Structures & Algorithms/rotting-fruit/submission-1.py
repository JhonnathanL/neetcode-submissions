from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        visited = set()
        queue = deque()
        fresh = 0

        def bfs(grid):
            nonlocal minutes
            nonlocal fresh

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            rows = len(grid)
            cols = len(grid[0])

            while queue and fresh > 0:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                            and (nr, nc) not in visited
                        ):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            grid[nr][nc] = 2
                            fresh -= 1

                minutes += 1

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2 and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i,j))
                
                elif grid[i][j] == 1:
                    fresh += 1

        bfs(grid)

        return minutes if fresh == 0 else -1
