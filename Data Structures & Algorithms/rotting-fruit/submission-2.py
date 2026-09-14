from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        queue = deque()

        minutes = 0
        fresh = 0

        def bfs(queue):
            nonlocal minutes
            nonlocal fresh

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            while queue and fresh > 0:

                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and grid[nr][nc] == 1
                        ):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            fresh -= 1

                minutes += 1

            return minutes if fresh == 0 else -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        return bfs(queue)