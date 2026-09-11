class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            seen_row = set()
            seen_col = set()

            for c in range(cols):

                if board[r][c] in seen_row and board[r][c] != ".":
                    return False

                seen_row.add(board[r][c])

                if board[c][r] in seen_col and board[c][r] != ".":
                    return False

                seen_col.add(board[c][r])

        for r in range(0, rows, 3):
            for c in range(0, cols, 3):

                box = set()

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] in box and board[i][j] != ".":
                            return False
                        
                        box.add(board[i][j])

        return True