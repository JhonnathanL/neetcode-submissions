class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            visited.add((r, c))

            region = []
            touches_edge = False

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ]

            while q:
                r, c = q.popleft()

                region.append((r, c))

                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    touches_edge = True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] == "O" and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return region, touches_edge


        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O" and (r, c) not in visited:

                    region, touches_edge = bfs(r, c)

                    if not touches_edge:
                        for rr, cc in region:
                            board[rr][cc] = "X"