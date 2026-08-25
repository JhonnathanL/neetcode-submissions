class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        # Linhas e colunas
        for r in range(rows):
            seen_row = set()
            seen_col = set()

            for c in range(cols):

                # Linha
                if board[r][c] in seen_row and board[r][c] != ".":
                    return False

                seen_row.add(board[r][c])

                # Coluna
                if board[c][r] in seen_col and board[c][r] != ".":
                    return False

                seen_col.add(board[c][r])

        # Quadrados 3x3
        for r in range(0, rows, 3):
            for c in range(0, cols, 3):

                seen_box = set()

                for i in range(3):
                    for j in range(3):

                        value = board[r + i][c + j]

                        if value in seen_box and value != ".":
                            return False

                        seen_box.add(value)

        return True