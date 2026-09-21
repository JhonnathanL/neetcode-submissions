class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows * cols) - 1


        while l <= r:

            mid = (l + r) // 2    

            row = mid // cols
            col = mid % cols

            curr = matrix[row][col]

            if curr == target:
                return True
            
            elif curr < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False
