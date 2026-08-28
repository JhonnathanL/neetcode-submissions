class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c, i):

            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            visited.remove((r, c))

            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False