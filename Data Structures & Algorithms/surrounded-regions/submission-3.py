from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        visited = set()

        rows = len(board)
        cols = len(board[0])

        def bfs(r, c):
            nonlocal visited

            queue = deque()
            queue.append((r,c))

            current = set()
            current.add((r,c))

            visited.add((r,c))

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

                    if (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr,nc) not in visited):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        current.add((nr,nc))
                    
            for nr, nc in current:    
                if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1):
                    break
            else:
                for nr, nc in current:
                    board[nr][nc] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    bfs(i,j)

